import pandas as pd
import numpy as np
from datetime import datetime
import os


class PPK_Processing_Result_DataLoader:
    def __init__(self, file_name:str) -> None:
        self.raw_data = pd.read_csv(file_name)
        self.data = self._setting()
        self.file_name = file_name
        self._remove_empty()
        self._seprates_to()
        self._remove_first_wrong_elements()

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
        self.data.replace(" ", np.NAN, inplace=True)
        self.data.dropna(inplace=True)
        self.data.index = range(len(self.data))

    def _seprates_to(self) -> None:
        text_files_data = []
        for i in range(len(self.data)):
            if self.data.loc[i]["No"] == 1:
                text_files_data.append([(self.data.loc[i]["No"], self.data.loc[i]["Latitude"], self.data.loc[i]["Longitude"], self.data.loc[i]["Height"])])
            else:
                text_files_data[-1].append((self.data.loc[i]["No"], self.data.loc[i]["Latitude"], self.data.loc[i]["Longitude"], self.data.loc[i]["Height"]))

        self.text_files_data = text_files_data

    def _remove_first_wrong_elements(self) -> None:
        wrong_text_file = []
        for text_file in self.text_files_data:
            wrong_text_file.append([])
            for i in range(len(text_file)):
                wrong_text_file[-1].append(i)
                if abs(float(text_file[i][3])-float(text_file[i+1][3])) > 1.5:
                    break
                if len(wrong_text_file[-1]) > 50:
                    wrong_text_file[-1] = []
                    break

        for i in range(len(wrong_text_file)):
            for j in reversed(wrong_text_file[i]):
                self.text_files_data[i].pop(j)
    
    def save(self, folder_name:str)->None:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        base_name = os.path.basename(self.file_name)
        base_name_without_ext = os.path.splitext(base_name)[0]
        PPK_file = os.path.join(folder_name, f"PPK_Processing_{base_name_without_ext}.csv")

        # Save the csv file
        self.data.to_csv(PPK_file, header=False, index=False)

        # Save the text file for different parts
        text_files = []
        for i in range(len(self.text_files_data)):
            text_files.append(os.path.join(folder_name, f"PPK_{base_name_without_ext}_file{i+1}.txt"))
            with open(text_files[-1], "w") as file:
                for row in list(self.text_files_data[i]):
                    file.write(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\n")

        # Save the text file for empty rows
        empty_file = os.path.join(folder_name, f"PPK_{base_name_without_ext}_empty_rows.txt")
        with open(empty_file, "w") as file:
            for row in list(self.empty_rows):
                file.write(f"{row}\n")

        return PPK_file, empty_file, text_files


            

