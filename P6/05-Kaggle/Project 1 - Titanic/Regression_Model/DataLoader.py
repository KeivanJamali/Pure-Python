import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import Information as info

class Dataloader:
    def __init__(self, data_path:Path, seed=42):
        np.random.seed(seed)
        self.seed = seed
        self.raw_data = pd.read_csv(data_path, index_col=0)
        self.data = self.raw_data.copy()
        self.set_setting()
        

    def set_setting(self):
        self.target = info.target
        # Both 'Fare' and 'Pclass' are showing the same thing. We need to include one of them only.
        # I chose 'Fare' because it is more specefic.
        self.features = info.features

        # male = 0, female = 1
        self.data["Sex"] = self.data["Sex"].map({"male":0, "female":1})

        # Age missing data: same distribution as the age data.
        age_values = self.data["Age"].dropna()
        missed_number = self.data["Age"].isna().sum()
        imputed_values = np.random.choice(age_values, size=missed_number, replace=True)
        self.data.loc[self.data["Age"].isna(), "Age"] = imputed_values

        # Embarked missing data.
        embarked_values = self.data["Embarked"].dropna()
        missed_number = self.data["Embarked"].isna().sum()
        imputed_values = np.random.choice(embarked_values, size=missed_number, replace=True)
        self.data.loc[self.data["Embarked"].isna(), "Embarked"] = imputed_values
        self.data["Embarked"] = self.data["Embarked"].map({"S":0, "C":1, "Q":2})

        self.data = self.data.loc[:, self.target+self.features]

    def _scale_data(self):
        self.scaler = MinMaxScaler()
        self.data[info.features] = self.scaler.fit_transform(self.data[info.features])