from sickle import Sickle
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from pathlib import Path
import os
from datetime import datetime
import numpy as np
import matplotlib.cm as cm


class SearchArxivOAI:
    _result_path = Path(__file__).parent / "result"

    def __init__(self, start_year, end_year, keyword_groups, group_names=None, max_number_in_year=10000):
        os.makedirs(SearchArxivOAI._result_path, exist_ok=True)
        self.start_year = start_year
        self.end_year = end_year
        self.keyword_groups = keyword_groups
        self.group_names = group_names or [f"Group_{i+1}" for i in range(len(keyword_groups))]
        self.max_number_in_year = max_number_in_year
        self.years = range(start_year, end_year + 1)
        self.sickle = Sickle("http://export.arxiv.org/oai2")
        self.saved_papers = {}
        self.count_data = {}
        self.count_percent = {}
        self.saved_papers_frame = None
        self.count_data_frame = None
        self.count_percent_frame = None
        

    @staticmethod
    def filter_record(record: dict, keywords: list) -> bool:
        """
        Returns True if any of the keywords appear in the title, abstract, or method/methodology section (if present).
        Checks for variations: 'method', 'methods', 'methodology', 'methodologies'.
        """
        meta = record.metadata
        title = " ".join(meta.get("title", [])).lower()
        abstract = " ".join(meta.get("description", [])).lower()

        for kw in keywords:
            kw_lower = kw.lower()
            if kw_lower in title or kw_lower in abstract:
                return True
        return False

    def fetch_arxiv_records(self, from_date: str, until_date: str):
        """
        Fetches arXiv records using Sickle for the given date range.
        Returns an iterator of records.
        """
        return self.sickle.ListRecords(
            **{"metadataPrefix": "oai_dc",
                "from": from_date,
                "until": until_date})

    def fit(self) -> tuple:
        """Loop over years and keyword groups, counting papers per year."""
        for group_name, keywords in zip(self.group_names, self.keyword_groups):
            self.count_data[group_name] = {}
            self.saved_papers[group_name] = {}
            self.count_percent[group_name] = {}
            for year in tqdm(self.years, desc=f"Searching for '{group_name}'"):
                try:
                    count, papers, total_record = self.get_group_count(keywords, year)
                    self.count_data[group_name][year] = count
                    self.count_percent[group_name][year] = (count / total_record) * 100 if total_record else 0
                    self.saved_papers[group_name][year] = papers
                except Exception as e:
                    print(f"Error for {group_name}-{year}: {e}")
                    self.count_data[group_name][year] = None
                    self.count_percent[group_name][year] = None

        self.count_data_frame = pd.DataFrame(self.count_data)
        self.count_data_frame.index.name = "Year"
        self.saved_papers_frame = pd.DataFrame(self.saved_papers)
        self.saved_papers_frame.index.name = "Year"
        self.count_percent_frame = pd.DataFrame(self.count_percent)
        self.count_percent_frame.index.name = "Year"

        self.count_data_frame.to_csv(SearchArxivOAI._result_path / "arxiv_language_group_counts.csv")
        self.count_percent_frame.to_csv(SearchArxivOAI._result_path / "arxiv_language_group_percent.csv")
        self.saved_papers_frame.to_csv(SearchArxivOAI._result_path / "arxiv_language_group_papers.csv")
        
        return self.count_data_frame, self.count_percent_frame, self.saved_papers_frame

    def get_group_count(self, keywords: list, year: int) -> tuple:
        """
        Counts unique papers mentioning any of the keywords in a given year.
        Each paper is counted once even if it matches multiple keywords.
        """
        seen_ids = set()
        papers = {}
        from_date = f"{year}-01-01"
        if year == datetime.now().year:
            until_date = datetime.now().strftime("%Y-%m-%d")
        else:
            until_date = f"{year}-12-31"

        records = self.fetch_arxiv_records(from_date, until_date)
        count = 0
        for record in records:
            count += 1
            if count >= self.max_number_in_year:
                break
            id_ = record.header.identifier
            title = " ".join(record.metadata.get("title", [])).lower()
            if self.filter_record(record, keywords):
                seen_ids.add(id_)
                papers[id_] = title

        return len(seen_ids), papers, count

    def plot_results(self, data: pd.DataFrame, name: str):
        plt.figure(figsize=(14, 7))

        # Basic setup
        n_groups = len(self.group_names)
        years = np.arange(len(data.index))
        bar_width = 0.12  # Adjust spacing between bars
        colors = plt.get_cmap('tab10').colors  # Good color map for categorical data
        
        # Plot each group
        for i, group in enumerate(self.group_names):
            positions = years + i * bar_width
            bars = plt.bar(
                positions,
                data[group],
                width=bar_width,
                label=group,
                color=colors[i % len(colors)],
                edgecolor='black',
                alpha=0.9
            )

            # Add numbers on each bar
            for bar in bars:
                height = bar.get_height()
                if height > 0:
                    if name == "counts":
                        plt.text(
                            bar.get_x() + bar.get_width() / 2,
                            height,
                            f"{int(height)}",
                            ha="center", va="bottom", fontsize=14, rotation=0
                        )
                    else:
                        plt.text(
                            bar.get_x() + bar.get_width() / 2,
                            height,
                            f"{height:.2f}",
                            ha="center", va="bottom", fontsize=14, rotation=0
                        )

        # Formatting
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Percentage of arXiv Papers (%)", fontsize=12)
        plt.title(f"Programming Language Mentions in arXiv Papers ({self.start_year}–{self.end_year})",
                fontsize=14, weight='bold')
        
        # X-ticks centered on groups
        plt.xticks(years + bar_width * (n_groups / 2 - 0.5), data.index, rotation=45)
        plt.legend(title="Language Groups", loc="upper left", bbox_to_anchor=(1, 1))
        plt.grid(True, axis='y', linestyle='--', alpha=0.3)
        plt.tight_layout()

        # Save and show
        plt.savefig(SearchArxivOAI._result_path / f"arxiv_language_{name}.png", dpi=300)
        plt.show()