from sickle import Sickle
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from pathlib import Path
import os
from datetime import datetime


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

    def fit(self):
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

    def get_group_count(self, keywords: list, year: int) -> int:
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

    def plot_results(self, data: pd.DataFrame):
        plt.figure(figsize=(12, 7))
        for group in self.group_names:
            plt.plot(data.index, data[group], label=group, marker='o')

        plt.xlabel("Year")
        plt.ylabel(f"Amount of arXiv papers mentioning groups")
        plt.title("ArXiv Papers (2000–2025)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(SearchArxivOAI._result_path / "arxiv_language_group_trends.png")
        plt.show()

