import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import Information as info

class Dataloader:
    def __init__(self, data_path:Path, seed=42):
        np.random.seed(seed)
        self.seed = seed
        self.raw_data = pd.read_csv(data_path, index_col=0)
        self.data = self.raw_data.copy()
        self.set_setting()
        # self._scale_data()

    def set_setting(self):
        self.target = info.target
        self.features = info.features
        self.one_hot_encoding_columns = info.one_hot_encoding
        self.data = self.data.loc[:, self.target+self.features]

        self.data["Street"] = self.data["Street"].map({"Grvl":2,
                                                       "Pave":1})
        self.data["Alley"] = self.data["Alley"].map({"Grvl":2,
                                                     "Pave":1})
        self.data["Alley"].fillna(0, inplace=True)
        self.data["MasVnrArea"].fillna(0, inplace=True)
        self.data["ExterCond"] = self.data["ExterCond"].map({"Ex":5,
                                                             "Gd":4,
                                                             "TA":3,
                                                             "Fa":2,
                                                             "Po":1})
        self.data["ExterQual"] = self.data["ExterQual"].map({"Ex":5,
                                                             "Gd":4,
                                                             "TA":3,
                                                             "Fa":2,
                                                             "Po":1})
        self.data["BsmtQual"] = self.data["BsmtQual"].map({"Ex":5,
                                                             "Gd":4,
                                                             "TA":3,
                                                             "Fa":2,
                                                             "Po":1})
        self.data["BsmtQual"].fillna(0, inplace=True)
        self.data["BsmtCond"] = self.data["BsmtCond"].map({"Ex":5,
                                                             "Gd":4,
                                                             "TA":3,
                                                             "Fa":2,
                                                             "Po":1})
        self.data["BsmtCond"].fillna(0, inplace=True)
        self.data["BsmtExposure"] = self.data["BsmtExposure"].map({
                                                             "Gd":4,
                                                             "Av":3,
                                                             "Mn":2,
                                                             "No":1})
        self.data["BsmtExposure"].fillna(0, inplace=True)
        self.data["BsmtFinType1"] = self.data["BsmtFinType2"].map({
                                                             "GLQ":6,
                                                             "ALQ":5,
                                                             "BLQ":4,
                                                             "Rec":3,
                                                             "LwQ":2,
                                                             "Unf":1})
        self.data["BsmtFinType1"].fillna(0, inplace=True)
        self.data["BsmtFinType2"] = self.data["BsmtFinType2"].map({
                                                             "GLQ":6,
                                                             "ALQ":5,
                                                             "BLQ":4,
                                                             "Rec":3,
                                                             "LwQ":2,
                                                             "Unf":1})
        self.data["BsmtFinType2"].fillna(0, inplace=True)
        self.data["HeatingQC"] = self.data["HeatingQC"].map({"Ex":5,
                                                             "Gd":4,
                                                             "TA":3,
                                                             "Fa":2,
                                                             "Po":1})
        self.data["CentralAir"] = self.data["CentralAir"].map({"Y":1,
                                                               "N":0})
        self.data["KitchenQual"] = self.data["KitchenQual"].map({"Ex":5,
                                                             "Gd":4,
                                                             "TA":3,
                                                             "Fa":2,
                                                             "Po":1})
        self.data["FireplaceQu"] = self.data["FireplaceQu"].map({"Ex":5,
                                                             "Gd":4,
                                                             "TA":3,
                                                             "Fa":2,
                                                             "Po":1})
        self.data["FireplaceQu"].fillna(0, inplace=True)
        self.data["GarageYrBlt"].fillna(0, inplace=True)
        self.data["GarageFinish"] = self.data["GarageFinish"].map({"Fin":3,
                                                                   "RFn":2,
                                                                   "Unf":1})
        self.data["GarageFinish"].fillna(0, inplace=True)
        self.data["GarageQual"] = self.data["GarageQual"].map({"Ex":5,
                                                             "Gd":4,
                                                             "TA":3,
                                                             "Fa":2,
                                                             "Po":1})
        self.data["GarageQual"].fillna(0, inplace=True)
        self.data["GarageCond"] = self.data["GarageCond"].map({"Ex":5,
                                                             "Gd":4,
                                                             "TA":3,
                                                             "Fa":2,
                                                             "Po":1})
        self.data["GarageCond"].fillna(0, inplace=True)
        self.data["PavedDrive"] = self.data["PavedDrive"].map({"Y":2,
                                                               "P":1,
                                                               "N":0})
        self.data["PoolQC"] = self.data["PoolQC"].map({"Ex":4,
                                                       "Gd":3,
                                                       "TA":2,
                                                       "Fa":1})
        self.data["PoolQC"].fillna(0, inplace=True)



        self.data = pd.get_dummies(self.data, columns=self.one_hot_encoding_columns, dtype=int)

    def _scale_data(self):
        self.scaler = MinMaxScaler()
        self.data[info.features] = self.scaler.fit_transform(self.data[info.features])