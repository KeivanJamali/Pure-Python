import pandas as pd
import numpy as np
import os
from sklearn.svm import SVC
code_name = "Generic"

plot_dir = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\plots'

class Generic_DataLoader:
    """Take the CSV file that include Point, Station, Offset and Elevation and produce the Generic file
    in the format of 
    chainage    station_no
    Offset      Elevation
    Offset      Elevation
    Offset      Elevation
    Offset      Elevation
    chainage    station_no
    Offset      Elevation
    Offset      Elevation
    Offset      Elevation
    Offset      Elevation
    chainage    station_no
    Offset      Elevation
    Offset      Elevation
    Offset      Elevation
    Offset      Elevation
    chainage    station_no
    Offset      Elevation
    Offset      Elevation
    Offset      Elevation
    Offset      Elevation
    """
    def __init__(self, file_name: str) -> None:
        """
        Initialize the data loader with a CSV file.

        Parameters:
        file_name (str): The path to the CSV file.
        """
        self.file_name = file_name
        self.raw_data = pd.read_csv(file_name)
        self._clean_data()
        self.generic = None
        self.zeros = []
        
    def _clean_data(self) -> None:
        """
        Clean the raw data by renaming columns, resetting the index,
        and removing NaN values.
        """
        self.data = self.raw_data.copy()
        self.data.columns = self.data.loc[12]
        self.data = self.data.iloc[13:,:-1]
        self.data.index = range(len(self.data))
        self._remove_nan()

        self._correct_station_values()
        self._correct_elevation_values()
        self._correct_offset_values()

    def _remove_nan(self) -> None:
        """
        Remove rows with NaN values and rows with 'Out of range' stations.
        """
        self.data.dropna(inplace=True)
        outranges = self.data[self.data["Station"] == "Out of range"].index
        self.outrange_id = list(self.data.loc[outranges]["Point"])
        self.data.drop(outranges, inplace=True)
    
    def _correct_station_values(self) -> None:
        """
        Correct station values by converting them to floats.
        """
        def station_apply(x):
            if "+" in str(x):
                return float("".join(str(x).split("+")))
            else:
                return float("-"+str(x))
        self.data["Station"] = self.data["Station"].apply(lambda x: station_apply(x))

    def _correct_offset_values(self) -> None:
        """
        Correct offset values by converting them to floats and removing the last character.
        """
        self.data["Offset"] = self.data["Offset"].apply(lambda x: float(str(x)[:-1]))

    def _correct_elevation_values(self) -> None:
        """
        Correct elevation values by converting them to floats and removing commas.
        """
        self.data["Elevation"] = self.data["Elevation"].apply(lambda x: float("".join(str(x)[:-1].split(","))))
        

    def _find_center_of_clusters(self, epsilon, round_lim) -> None:
        """
        Find the center of clusters within the data based on station and offset values.

        Parameters:
        epsilon (float): The threshold for considering offsets as centered.
        round_lim (float): The rounding limit for station values.
        """
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

    def _generic_format(self, epsilon:float) -> pd.DataFrame:
        """
        Convert the data into a generic format suitable for further analysis.

        Parameters:
        epsilon (float): The threshold for considering offsets as centered.

        Returns:
        pd.DataFrame: The data in the generic format.
        """
        result = []
        map_data = []
        unique_clusters = self.center_points.sort_values(by="Station").index
        for cluster_id in unique_clusters:
            cluster_data = self.data[self.data["Cluster"] == cluster_id]
            center_station = self.center_points.loc[cluster_id, 'Station']
            cluster_data = cluster_data.sort_values(by='Offset')
            if len(cluster_data)==0:
                self.zeros.append(center_station)
                continue
            result.append(["chainage", center_station])

            number_of_zeros = 0
            lowest_offset = float("inf")
            for _, row in cluster_data.iterrows():
                if abs(row["Offset"]) < epsilon:
                    number_of_zeros += 1
                    if lowest_offset > abs(row["Offset"]):
                        lowest_offset = abs(row["Offset"])

            if number_of_zeros < 2:
                for _, row in cluster_data.iterrows():
                    if abs(row["Offset"]) < epsilon:
                        result.append([0, row["Elevation"]])
                        map_data.append([center_station, 0, row["Elevation"]])
                    else:
                        result.append([row["Offset"], row["Elevation"]])
                        map_data.append([center_station, row["Offset"], row["Elevation"]])
            else:
                for _, row in cluster_data.iterrows():
                    if abs(row["Offset"])-lowest_offset <= 0:
                        result.append([0, row["Elevation"]])
                        map_data.append([center_station, 0, row["Elevation"]])
                    else:
                        result.append([row["Offset"], row["Elevation"]])
                        map_data.append([center_station, row["Offset"], row["Elevation"]])
        result = pd.DataFrame(result)
        self.map_data = pd.DataFrame(map_data, columns=["Station", "Offset", "Elevation"])
        return result
    
    def save_files(self, folder_name:str) -> tuple[str,str,str,str]:
        """
        Save the processed data to CSV and text files in the specified folder.

        Parameters:
        folder_name (str): The path to the folder where the files will be saved.

        Returns:
        tuple: Paths to the saved CSV, text, out-of-range, and zeros files.
        """
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        base_name = os.path.basename(self.file_name)
        base_name_without_ext = os.path.splitext(base_name)[0]

        # Save the CSV file
        csv_file = os.path.join(folder_name, f"{code_name}_{base_name}")
        self.generic.to_csv(csv_file, index=False, header=False)

        # Save the text file
        txt_file = os.path.join(folder_name, f"{code_name}_{base_name_without_ext}.txt")
        with open(txt_file, "w") as file:
            for _, row in self.generic.iterrows():
                file.write(f"{row[0]}\t{row[1]}\n")

        # Save the text file for out of ranges
        out_ranges_file = os.path.join(folder_name, f"{code_name}_{base_name_without_ext}_outranges.txt")
        with open(out_ranges_file, "w") as file:
            file.write("Out of ranges points which have no data in the input file.\n")
            file.write(f"Point\n")
            for row in self.outrange_id:
                file.write(f"{row}\n")

        # Save the text file for zeros
        zeros_file = os.path.join(folder_name, f"{code_name}_{base_name_without_ext}_zeros.txt")
        with open(zeros_file, "w") as file:
            file.write("If there is some station with no member inside, this node will ommited. The station will apeare here.\n")
            file.write("It can be for the reason that two same station be the main in clustering. In fact, the treshold for Epsilon is no accurate.\n")
            file.write(f"Station\n")
            for row in self.zeros:
                file.write(f"{row}\n")

        return csv_file, txt_file, out_ranges_file, zeros_file

    def fit(self, epsilon:float, round_lim:float) -> None:
        """
        Fit the data to find the center of clusters and convert it to the generic format.

        Parameters:
        epsilon (float): The threshold for considering offsets as centered.
        round_lim (float): The rounding limit for station values.
        """
        self._find_center_of_clusters(epsilon=epsilon, round_lim=round_lim)
        self.generic = self._generic_format(epsilon=epsilon)


