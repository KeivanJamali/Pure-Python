from tokenize import group
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

class DataLoader:
    needed_col = ["Note", "Latitude", "Longitude", "Ell.Height (m)"]
    def __init__(self, filepath: str, time_threshold: float = 5, elevation_threshold: float = None):
        self.filepath = Path(filepath)
        self.data = self._load_data()
        self._extract_date()
        self.group_data = self._separate_data()
        if elevation_threshold:
            self.removed_notes = self._remove_by_min_elevation(elevation_threshold)
        else:
            self.removed_notes = self._remove_by_std_deviation()
        self._remove_by_time(time_threshold=time_threshold)
        self._remove_empty_groups()
        print(f"Removed notes: {self.removed_notes}")

    def _load_data(self):
        if not self.filepath.exists():
            raise FileNotFoundError(f"The file {self.filepath} does not exist.")
        
        try:
            data = pd.read_csv(self.filepath)
            # Replace " " with np.nan for all columns
            data.replace(" ", pd.NA, inplace=True)
            # Convert columns to float, ignoring errors (NaNs will remain)
            data["Latitude"] = pd.to_numeric(data["Latitude"], errors="coerce")
            data["Longitude"] = pd.to_numeric(data["Longitude"], errors="coerce")
            data["Ell.Height (m)"] = pd.to_numeric(data["Ell.Height (m)"], errors="coerce")
            return data
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

    def _extract_date(self):
        self.data[["id", "date", "time", "time_part"]] = self.data["Name"].str.split(" ", expand=True)
        self.data["date"] = pd.to_datetime(self.data["date"] + " " + self.data["time"] + " " + self.data["time_part"],
                                           format="%Y-%m-%d %I:%M:%S.%f %p")
        self.data.sort_values(by=["date"], inplace=True, ignore_index=True)

    def _separate_data(self):
        df = self.data.copy()

        start_indices = df.index[df['Note'] == 1].tolist()
        group_data = []

        for i, start in enumerate(start_indices):
            end = start_indices[i+1] if i+1 < len(start_indices) else len(df)
            group = df.iloc[start:end]
            group_data.append(group)

        return group_data

    def _remove_by_std_deviation(self):
        removed_notes = {}
        for idx, group in enumerate(self.group_data):
            elevs = group["Ell.Height (m)"].dropna().astype(float)
            if elevs.empty:
                removed_notes[idx+1] = []
                continue
            mean_elev = elevs.mean()
            std_elev = elevs.std()
            # Find first index close to mean (within 1 std), or closest
            start = 0
            while start < len(group):
                elev = group.iloc[start]["Ell.Height (m)"]
                if pd.isna(elev):
                    start += 1
                    continue
                if abs(elev - mean_elev) <= 2*std_elev:
                    break
                start += 1
            # Find last index close to mean (within 1 std), or closest
            end = len(group) - 1
            while end >= start:
                elev = group.iloc[end]["Ell.Height (m)"]
                if pd.isna(elev):
                    end -= 1
                    continue
                if abs(elev - mean_elev) <= 2*std_elev:
                    break
                end -= 1
            # Remove notes outside main segment, store both Note and Elevation
            removed = []
            for i in range(0, start):
                removed.append({"data_num": idx + 1,
                    "Note": int(group.iloc[i]["Note"]),
                    "Elevation": float(group.iloc[i]["Ell.Height (m)"])
                })
            for i in range(end+1, len(group)):
                removed.append({
                    "data_num": idx + 1,
                    "Note": int(group.iloc[i]["Note"]),
                    "Elevation": float(group.iloc[i]["Ell.Height (m)"])
                })
            group = group.iloc[start:end+1].reset_index(drop=True)
            removed_notes[len(removed_notes) + 1] = removed
            self.group_data[idx] = group
        return removed_notes

    def _remove_by_min_elevation(self, min_elevation: float):
        removed_notes = {}
        for idx, group in enumerate(self.group_data):
            start = 0
            while start < len(group):
                elev = group.iloc[start]["Ell.Height (m)"]
                if pd.notna(elev) and elev < min_elevation:
                    start += 1
                else:
                    break
            end = len(group) - 1
            while end >= start:
                elev = group.iloc[end]["Ell.Height (m)"]
                if pd.notna(elev) and elev < min_elevation:
                    end -= 1
                else:
                    break
            # Store both Note and Elevation for removed points
            removed = []
            for i in range(0, start):
                removed.append({"data_num": idx + 1,
                    "Note": int(group.iloc[i]["Note"]),
                    "Elevation": float(group.iloc[i]["Ell.Height (m)"])
                })
            for i in range(end+1, len(group)):
                removed.append({
                    "data_num": idx + 1,
                    "Note": int(group.iloc[i]["Note"]),
                    "Elevation": float(group.iloc[i]["Ell.Height (m)"])
                })
            group = group.iloc[start:end+1].reset_index(drop=True)
            removed_notes[len(removed_notes) + 1] = removed
            self.group_data[idx] = group
            
        return removed_notes

    def _remove_by_time(self, time_threshold: int):
        for idx, group in enumerate(self.group_data):
            removed = []
            # Remove sparse data at the start
            start = 0
            while start + 1 < len(group):
                time_diff = (group.iloc[start + 1]["date"] - group.iloc[start]["date"]).total_seconds() / 60
                if time_diff > time_threshold:
                    # Remove all data up to and including start
                    for i in range(0, start + 1):
                        removed.append({"data_num": idx + 1,
                            "Note": int(group.iloc[i]["Note"]),
                            "Elevation": float(group.iloc[i]["Ell.Height (m)"])
                        })
                    group = group.iloc[start + 1:].reset_index(drop=True)
                    start = 0
                else:
                    start += 1
            # Remove sparse data at the end
            end = len(group) - 1
            while end > 0:
                time_diff = (group.iloc[end]["date"] - group.iloc[end - 1]["date"]).total_seconds() / 60
                if time_diff > time_threshold:
                    # Remove all data from end to the last
                    for i in range(end, len(group)):
                        removed.append({"data_num": idx + 1,
                            "Note": int(group.iloc[i]["Note"]),
                            "Elevation": float(group.iloc[i]["Ell.Height (m)"])
                        })
                    group = group.iloc[:end].reset_index(drop=True)
                    end = len(group) - 1
                else:
                    end -= 1
            if removed:
                self.removed_notes[len(self.removed_notes) + 1] = removed
            if not group.empty:
                self.group_data[idx] = group

    def _remove_empty_groups(self):
        non_empty_groups = []
        for i in range(len(self.group_data)):
            group = self.group_data[i]
            if not group.empty:
                non_empty_groups.append(group)
        self.group_data = non_empty_groups

    def store_data(self, output_dir: str, start_num: int):
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        for idx, group in enumerate(self.group_data):
            rows = group[self.needed_col].dropna().shape[0]
            out_file = output_path / f"{start_num + idx}_{rows}.txt"
            # save as .txt without header or index
            group[self.needed_col].dropna().to_csv(out_file, index=False, header=False)
        removed_rows = []
        for notes in self.removed_notes.values():
            for note in notes:
                removed_rows.append({
                    "data_num": note["data_num"],
                    "Note": note["Note"],
                    "Elevation": note["Elevation"]
                })
        if removed_rows:
            removed_data = pd.DataFrame(removed_rows)
            removed_data.to_csv(output_path / "removed_notes.txt", index=False, header=True)

class Engine:
    def __init__(self):
        pass
    
    def plot_data(self, data: pd.DataFrame, idx: int):
        data["Solution Type"].fillna("None", inplace=True)
        # Pie chart for Solution Type
        solution_counts = data['Solution Type'].value_counts()
        print(solution_counts)
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(
            solution_counts,
            labels=solution_counts.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=["#4CAF50", "#FFC107", "#F44336"],
            wedgeprops={"edgecolor": "white", "linewidth": 2},
            textprops={"fontsize": 12}
        )
        ax.set_title(f'Group {idx} - Solution Type Distribution', fontsize=14, fontweight='bold')
        # Add total record count below the plot
        total_records = len(data)
        plt.figtext(0.5, 0.01, f"Total records: {total_records}", ha="center", fontsize=12, color="gray")
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
        
        # Elevation analysis (histogram with counts on bars)
        elev = data['Ell.Height (m)'].dropna().astype(float)
        fig, ax = plt.subplots(figsize=(7, 5))
        n, bins, patches = ax.hist(elev, bins=30, color="#4A90E2", edgecolor="white", alpha=0.85)
        ax.set_title(f'Group {idx} - Elevation Distribution', fontsize=14, fontweight='bold')
        ax.set_xlabel('Ell.Height (m)', fontsize=12)
        ax.set_ylabel('Count', fontsize=12)
        # Annotate each bar with its count
        for i in range(len(patches)):
            if n[i] > 0:
                ax.text(
                    (bins[i] + bins[i+1]) / 2,
                    n[i],
                    str(int(n[i])),
                    ha='center', va='bottom', fontsize=10, color='black', fontweight='bold', rotation=0
                )
        # Add total record count below the plot
        plt.figtext(0.5, 0.01, f"Total records: {len(elev)}", ha="center", fontsize=12, color="gray")
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

        # Elevation vs. Time plot
        if 'date' in data.columns and 'Ell.Height (m)' in data.columns:
            elev_time = data[['date', 'Ell.Height (m)']].dropna()
            elev_time['Ell.Height (m)'] = elev_time['Ell.Height (m)'].astype(float)
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(elev_time['date'], elev_time['Ell.Height (m)'], marker='o', linestyle='-', color='#009688', alpha=0.7)
            ax.set_title(f'Group {idx} - Elevation Over Time', fontsize=14, fontweight='bold')
            ax.set_xlabel('Time', fontsize=12)
            ax.set_ylabel('Ell.Height (m)', fontsize=12)
            ax.grid(True, linestyle='--', alpha=0.5)
            plt.figtext(0.5, 0.01, f"Total records: {len(elev)}", ha="center", fontsize=12, color="gray")
            plt.tight_layout(rect=[0, 0.03, 1, 0.95])
            plt.show()
        
        