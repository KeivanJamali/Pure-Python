import pandas as pd
import os

class Generic_DataLoader:
    def __init__(self, file_name: str, threshold:float=0.2) -> None:
        self.file_name = file_name
        self.data = self._set_data_preparation(file_name=file_name)
        self.total_nodes = len(self.data)
        self.clusters = self._make_cluster()
        self.final_clusters = self._reorder_clusters(threshold=threshold)
        self.generic = self._fit_format()

    def _set_data_preparation(self, file_name:str) -> None:
        data = pd.read_csv(file_name)
        self.raw_data = data.copy()
        data = data.iloc[13:, :-1]
        data.columns = ["Point", "Station", "Offset", "Elevation"]
        out_of_range = data[data["Station"] == "Out of range"].index
        self.out_of_range_data = list(data.loc[out_of_range]["Point"])
        data.drop(out_of_range, inplace=True)
        data.dropna(inplace=True)
        data["Station_new"] = data["Station"].apply(lambda x: float("".join(str(x).split("+"))))
        data["Offset_new"] = data["Offset"].apply(lambda x: float(str(x)[:-1]))
        data["Elevation_new"] = data["Elevation"].apply(lambda x: float("".join(str(x)[:-1].split(","))))
        data = data.sort_values(by="Station_new")
        data = data.iloc[:, -3:]
        data.columns = ["Station", "Offset", "Elevation"]
        data.index = range(len(data.index))
        return data
    
    def _check_offset(self, offset: float, threshold: float) -> bool:
        if abs(offset) <= threshold:
            return True
        else:
            return False
        
    def _check_distance(self, node_id: int) -> bool:
        distance_to_pre = self.data["Station"][node_id]-self.data["Station"][node_id-1]
        dictance_to_next = self.data["Station"][node_id+1]-self.data["Station"][node_id]
        if abs(dictance_to_next-distance_to_pre) > 2:
            return True
        else:
            return False

    def _make_cluster(self) -> list:
        clusters = []
        cluster_id = -1
        node_id = -1
        break_happens = 0
        while node_id < self.total_nodes-1:
            cluster_id += 1
            clusters.append([])
            while True:
                node_id += 1
                clusters[cluster_id].append(node_id)
                if node_id == self.total_nodes-1:
                    break
                elif node_id > 1 and self._check_distance(node_id=node_id):
                    break_happens += 1
                    if break_happens%2 == 1:
                        break
        return clusters

    def _aproximate_station_name(self, cluster_id:int) -> str:
        stations = self.data.loc[self.clusters[cluster_id]]["Station"]
        offsets = self.data.loc[self.clusters[cluster_id]]["Offset"]
        mean_name = sum(stations)/len(stations)
        if mean_name%10 < 1.2 or mean_name%10 > 8.8:
            return round(mean_name)
        else:
            return "Wait"
    
    def _reorder_clusters(self, threshold:float) -> list:
        clusters_inshape = []
        for cluster_id in range(len(self.clusters)):
            station_name = self._aproximate_station_name(cluster_id)
            station_new = [station_name for _ in range(len(self.clusters[cluster_id]))]
            temp_offset = self.data.loc[self.clusters[cluster_id]]["Offset"]
            temp_elevation = self.data.loc[self.clusters[cluster_id]]["Elevation"]
            temp_stations = self.data.loc[self.clusters[cluster_id]]["Station"]
            data_need_sorting = list(zip(station_new, self.clusters[cluster_id], temp_offset, temp_elevation))
            # Check if there is very low offset in clustter!?
            choices = []
            done = False
            for i in range(len(data_need_sorting)):
                if self._check_offset(data_need_sorting[i][2], threshold=threshold):
                    choices.append([i, data_need_sorting[i][2], data_need_sorting[i][3]])
                    done = True
            if done:
                temp_min = min(choices, key=lambda x: x[1])
                station_name = data_need_sorting[0][0]
                if station_name == "Wait":
                    station_name = list(temp_stations)[temp_min[0]]
                exact = (station_name, 0, 0, temp_min[2])
                data_need_sorting.pop(temp_min[0])
            # find the weighted average of the max negetive and min positive offsets.
            if not done:
                temp_pos_offset = float("inf")
                temp_neg_offset = float("inf")
                for i in range(len(data_need_sorting)):
                    temp_offset = data_need_sorting[i][2]
                    if temp_offset > 0:
                        if temp_offset < temp_pos_offset:
                            temp_pos_offset = temp_offset
                            temp_pos_offset_id = i
                    elif temp_offset < 0:
                        temp_offset = -temp_offset
                        if temp_offset < temp_neg_offset:
                            temp_neg_offset = temp_offset
                            temp_neg_offset_id = i

                station_name = data_need_sorting[0][0]
                if station_name == "Wait":
                    station_name = (temp_stations[temp_pos_offset_id] + temp_stations[temp_neg_offset_id])/2
                exact = (station_name, 0, 0, (temp_pos_offset*data_need_sorting[temp_pos_offset_id][3] + temp_neg_offset*data_need_sorting[temp_neg_offset_id][3])/(temp_pos_offset+temp_neg_offset))
            # replace the exact value for offset 0.
            data_need_sorting.append(exact)
            sorted_data = sorted(list(data_need_sorting), key=lambda x: x[2])
            clusters_inshape.append(sorted_data)
        return clusters_inshape
    
    def _fit_format(self) -> pd.DataFrame:
        final_result = []
        for cluster in self.final_clusters:
            for row in cluster:
                if type(row[0]) != str:
                    station_name = row[0]
                    break
            final_result.append(["chainage", cluster[0][0]])
            for node in cluster:
                final_result.append([node[2], node[3]])
        result = pd.DataFrame(final_result)
        return result
    
    def save_file(self, folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the excel file
        self.generic.to_csv(f"{folder_name}/generic_{self.file_name.split("/")[-1]}", index=False, header=False)

        # save the text file
        temp_address = f"{folder_name}/generic_{self.file_name.split("/")[-1][:-3]}txt"
        with open(temp_address, "w") as file:
            for _, row in self.generic.iterrows():
                file.write(f"{row[0]}\t{row[1]}\n")

        # save the text file for out of ranges.
        temp_address = f"{folder_name}/generic_{self.file_name.split("/")[-1][:-4]}_outranges.txt"
        with open(temp_address, "w") as file:
            for row in self.out_of_range_data:
                file.write(f"{row}\n")

    staticmethod
    def _mean(data):
        return sum(data)/len(data)
    

file = "D10 points.csv"
dataloader = Generic_DataLoader(file_name=file, threshold=0.2)
dataloader.save_file("result")