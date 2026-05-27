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
        self._scale_data()

    def set_setting(self):
        self.target = info.target
        self.features = info.features
        self.data = self.data.loc[:, self.target+self.features]

    def _scale_data(self):
        self.scaler = MinMaxScaler()
        self.data[info.features] = self.scaler.fit_transform(self.data[info.features])