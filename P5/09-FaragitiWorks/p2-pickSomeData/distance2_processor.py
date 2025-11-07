import pandas as pd
from pathlib import Path

class Dataloader_Distance:
    def __init__(self, file_path: Path):
        data = pd.read_excel(file_path, sheet_name="Project coordinates")
        headers = data.iloc[2, :].values
        data.columns = headers
        data.drop([0, 1, 2], axis=0, inplace=True)
        data.index = range(len(data))
        self.data = data
        
    def fit(self, cols: str):
        col_names = self.extract_columns(cols)
        data = self.data[["Distance"]+col_names].copy()
        new_data = pd.DataFrame(columns=["Distance", "Offset", "Elevation"])
        for i, row in data.iterrows():
            if i % 2 == 1:
                continue
            distance = float(row["Distance"])
            for col in col_names:
                if col[0] == "L":
                    offset = -row[col]
                elevation = data.iloc[i+1, :][col]
                new_data.loc[len(new_data)] = {"Distance": distance, "Offset": offset, "Elevation": elevation}
        new_data.sort_values(by=["Distance", "Offset"], inplace=True)
        new_data.to_csv("processed_data.csv", index=False)
        return new_data


    def extract_columns(self, cols: str):
        if ":" in cols:
            start, stop = cols.split(":")
            start, stop = start.strip(), stop.strip()
            if start[0] == "L" and stop[0] == "L":
                col_names = [f"L{i}" for i in range(int(start[1:]), int(stop[1:]) - 1, -1)]
            elif start[0] == "L" and stop[0] == "R":
                col_names = [f"L{i}" for i in range(int(start[1:]), 0, -1)] + [f"R{i}" for i in range(1, int(stop[1:]) + 1)]
            elif start[0] == "R" and stop[0] == "R":
                col_names = [f"R{i}" for i in range(int(start[1:]), int(stop[1:]) + 1)]
        else:
            col_names = cols.split(",")
            temp = []
            for col in col_names:
                temp.append(col.strip())
            col_names = temp
        
        return col_names



