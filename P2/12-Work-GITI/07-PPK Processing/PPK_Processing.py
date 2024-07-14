import pandas as pd
from datetime import datetime


class PPK_Processing_Result_DataLoader:
    def __init__(self, file_name:str) -> None:
        self.raw_data = pd.read_csv(file_name)
        self.data = self._setting()

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
    
    def save(self, output_file_name:str)->None:
        resutl = self.data.iloc[:, :-1]
        resutl.to_csv(output_file_name, header=False, index=False)


            

