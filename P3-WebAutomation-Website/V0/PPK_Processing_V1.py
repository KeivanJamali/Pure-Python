import pandas as pd
import numpy as np
from datetime import datetime
import os
code_name = "PPK"


class PPK_Processing_Result_DataLoader:
    def __init__(self, file_name:str, minutes_limit, height_limit) -> None:
        self.raw_data = pd.read_csv(file_name)
        self.data = self._setting()
        self.file_name = file_name
        self._remove_empty()
        self._remove_first_wrong_elements(minutes_limit, height_limit)

    def _setting(self):
        date = []
        am_pm = []
        for i in range(len(self.raw_data)):
            temp = self.raw_data.loc[i]["Name"].split(" ")
            date.append(temp[1] + " " + temp[2])
            am_pm.append(temp[3])
        self.test = date
        data_date = pd.DataFrame({'date': date, 'am_pm': am_pm})
        data_date["datetime"] = pd.to_datetime(data_date.date, format='%Y-%m-%d %H:%M:%S.%f')
        self.test2 = data_date["datetime"]
        data_date.loc[data_date['am_pm'] == 'PM', 'datetime'] += pd.Timedelta(hours=12)
        data = pd.DataFrame({"No":self.raw_data["Note"], "Latitude":self.raw_data["Latitude"], "Longitude":self.raw_data["Longitude"], "Height":self.raw_data["Ell.Height (m)"], "Date":data_date["datetime"]})
        return data.sort_values("Date")
    
    def _remove_empty(self) -> None:
        self.empty_rows = self.data[self.data["Latitude"] == " "].index
        self.data.replace(" ", np.nan, inplace=True)
        self.data.dropna(inplace=True)
        self.data.index = range(len(self.data))

    def _remove_first_wrong_elements(self, minutes_limit=5, height_limit=1.5) -> None:
        result_files = [[0]]
        for i in range(1, len(self.data)):
            if (self.data.iloc[i, 4] - self.data.iloc[i-1, 4]).seconds < minutes_limit*60:
                result_files[-1].append(i)
            else:

                result_files.append([i])

        first_subs = []
        for sublist in result_files:
            first_subs.append([sublist[0]])
            for i in range(1, len(sublist)):
                if self.data.iloc[i, 3] - self.data.iloc[i-1, 3] < height_limit:
                    first_subs[-1].append(sublist[i])
                else:
                    break
            if len(first_subs[-1]) > 5:
                first_subs[-1] = []
        self.text_files_data = result_files
        self.wrong_data = [i for sub in first_subs for i in sub]
        return self.text_files_data, self.wrong_data

    
    def save_files(self, folder_name:str)->None:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        base_name = os.path.basename(self.file_name)
        base_name_without_ext = os.path.splitext(base_name)[0]
        PPK_file = os.path.join(folder_name, f"{code_name}_{base_name_without_ext}.csv")

        # Save the csv file
        self.data.to_csv(PPK_file, header=False, index=False)

        # Save the text file for different parts
        text_files = []
        one_line_file = []
        for i in range(len(self.text_files_data)):
            if len(self.text_files_data[i]) < 2:
                one_line_file.append(self.text_files_data[i][0])
                continue
            difference = [item for item in self.text_files_data[i] if item not in self.wrong_data]
            text_files.append(os.path.join(folder_name, f"{i+1}-{len(difference)}.txt"))
            with open(text_files[-1], "w") as file:
                for row in difference:
                    file.write(f"{self.data.loc[row][0]}\t{self.data.loc[row][1]}\t{self.data.loc[row][2]}\t{self.data.loc[row][3]}\n")

        # Save the text file for empty rows
        empty_file = os.path.join(folder_name, f"{code_name}_{base_name_without_ext}_deleted_rows.txt")
        with open(empty_file, "w") as file:
            file.write("Empty rows:\n")
            for row in list(self.empty_rows):
                file.write(f"{row}\n")
            file.write("Wrong rows:\n")
            for row in self.wrong_data:
                file.write(f"{row}\t{self.data.loc[row][0]}\t{self.data.loc[row][1]}\t{self.data.loc[row][2]}\t{self.data.loc[row][3]}\n")
            file.write("File with only one line:\n")
            for row in one_line_file:
                file.write(f"{row}\t{self.data.loc[row][0]}\t{self.data.loc[row][1]}\t{self.data.loc[row][2]}\t{self.data.loc[row][3]}\n")
                
        return PPK_file, empty_file, text_files
    
    def _make_final_folders(self, minutes_limit):
        result_files = [[self.files[0]]]
        for i in range(1, len(self.files)):
            if (self.images_date[i] - self.images_date[i-1]).seconds < minutes_limit*60:
                result_files[-1].append(self.files[i])
            else:
                result_files.append([self.files[i]])

        first_images = []
        for sublist in result_files:
            first_images.append(sublist.pop(0))

        return result_files, first_images
