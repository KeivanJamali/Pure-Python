import pandas as pd
import numpy as np
import os
from sklearn.svm import SVC



class Generic_DataLoader:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.raw_data = pd.read_csv(file_name)
        self._clean_data()
        self.generic = None
        self.zeros = []
        
    def _clean_data(self):
        self.data = self.raw_data.copy()
        self.data.columns = self.data.loc[12]
        self.data = self.data.iloc[13:,:-1]
        self.data.index = range(len(self.data))
        self._remove_nan()

        self._correct_station_values()
        self._correct_elevation_values()
        self._correct_offset_values()

    def _remove_nan(self) -> None:
        self.data.dropna(inplace=True)
        outranges = self.data[self.data["Station"] == "Out of range"].index
        self.outrange_id = outranges
        self.data.drop(outranges, inplace=True)
    
    def _correct_station_values(self) -> None:
        self.data["Station"] = self.data["Station"].apply(lambda x: float("".join(str(x).split("+"))))

    def _correct_offset_values(self) -> None:
        self.data["Offset"] = self.data["Offset"].apply(lambda x: float(str(x)[:-1]))

    def _correct_elevation_values(self) -> None:
        self.data["Elevation"] = self.data["Elevation"].apply(lambda x: float("".join(str(x)[:-1].split(","))))
        

    def _find_center_of_clusters(self, epsilon, round_lim) -> None:
        center_points = self.data[np.abs(self.data["Offset"]) < epsilon]
        center_points["Station"] = center_points["Station"].apply(lambda x: x if round_lim <= x % 10 <= (10-round_lim) else int(round(x/10)*10))
        self.center_points = center_points
        x_train = center_points[["Station"]].values
        y_train = center_points.index

        x_total = self.data[["Station"]].values

        svm_model = SVC(kernel="linear", C=1)
        svm_model.fit(x_train, y_train)
        predicted_clusters = svm_model.predict(x_total)
        self.data["Cluster"] = predicted_clusters

    def _generic_format(self, epsilon):
        result = []
        unique_clusters = self.center_points.sort_values(by="Station").index
        for cluster_id in unique_clusters:
            cluster_data = self.data[self.data["Cluster"] == cluster_id]
            center_station = self.center_points.loc[cluster_id, 'Station']
            cluster_data = cluster_data.sort_values(by='Offset')
            if len(cluster_data)==0:
                self.zeros.append(center_station)
                continue
            result.append(["chainage", center_station])
            for _, row in cluster_data.iterrows():
                if abs(row["Offset"]) < epsilon:
                    result.append([0, row["Elevation"]])
                else:
                    result.append([row["Offset"], row["Elevation"]])
        result = pd.DataFrame(result)
        return result
    
    def save_file(self, folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        base_name = os.path.basename(self.file_name)
        base_name_without_ext = os.path.splitext(base_name)[0]

        # Save the CSV file
        csv_file = os.path.join(folder_name, f"generic_{base_name}")
        self.generic.to_csv(csv_file, index=False, header=False)

        # Save the text file
        txt_file = os.path.join(folder_name, f"generic_{base_name_without_ext}.txt")
        with open(txt_file, "w") as file:
            for _, row in self.generic.iterrows():
                file.write(f"{row[0]}\t{row[1]}\n")

        # Save the text file for out of ranges
        out_ranges_file = os.path.join(folder_name, f"generic_{base_name_without_ext}_outranges.txt")
        with open(out_ranges_file, "w") as file:
            for row in self.outrange_id:
                file.write(f"{row}\n")

        # Save the text file for zeros
        zeros_file = os.path.join(folder_name, f"generic_{base_name_without_ext}_zeros.txt")
        with open(zeros_file, "w") as file:
            for row in self.zeros:
                file.write(f"{row}\n")

        return csv_file, txt_file, out_ranges_file

    def fit(self, epsilon, round_lim):
        self._find_center_of_clusters(epsilon=epsilon, round_lim=round_lim)
        self.generic = self._generic_format(epsilon=epsilon)

