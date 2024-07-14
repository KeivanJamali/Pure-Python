import pandas as pd
from datetime import datetime
import os


class PPK_Processing_Result_DataLoader:
    def __init__(self, file_name:str) -> None:
        self.raw_data = pd.read_csv(file_name)
        self.data = self._setting()
        self.file_name = file_name

    def _setting(self):
        date = []
        am_pm = []
        for i in range(len(self.raw_data)):
            temp = self.raw_data.loc[i]["Name"].split(" ")
            date.append(temp[1] + " " + temp[2])
            am_pm.append(temp[3])
        data_date = pd.DataFrame({'date': date, 'am_pm': am_pm})
        data_date["datetime"] = pd.to_datetime(data_date.date, format='%Y-%m-%d %I:%M:%S.%f')
        data_date.loc[data_date['am_pm'] == 'pm', 'datetime'] += pd.Timedelta(hours=12)
        data = pd.DataFrame({"No":self.raw_data["Note"], "Latitude":self.raw_data["Latitude"], "Longitude":self.raw_data["Longitude"], "Height":self.raw_data["Ell.Height (m)"], "Date":data_date["datetime"]})
        return data.sort_values("Date").iloc[:, :-1]
    
    def save(self, folder_name:str)->None:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        base_name = os.path.basename(self.file_name)
        base_name_without_ext = os.path.splitext(base_name)[0]
        PPK_file = os.path.join(folder_name, f"PPK_Processing_{base_name_without_ext}.csv")
        self.data.to_csv(PPK_file, header=False, index=False)
        return PPK_file


            

