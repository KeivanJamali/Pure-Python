import pandas as pd
import numpy as np
from itertools import product
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import Dataset, DataLoader
import torch
from ast import literal_eval
from tqdm.auto import tqdm



class MyDataset(Dataset):
    def __init__(self, data: pd.DataFrame):
        features = ["OverallQual", "YearBuilt", "LotArea", "Heating_GasA", "Heating_GasW", "Heating_Grav", "Heating_OthW", "Heating_Wall"]
        target = ["SalePrice"]
        self.data = data
        for col in features + target:
            data[col] = torch.tensor(data[col].values, dtype=torch.float)
        self.x, self.y = self.data[features].values, self.data[target].values

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return torch.tensor(self.x[idx], dtype=torch.float), torch.tensor(self.y[idx], dtype=torch.float)


class MyDataloader:
    def __init__(self, 
                 data_path: Path, 
                 train_percent: float, 
                 val_percent: float, 
                 test_percent: float, 
                 batch_size: int, 
                 seed: int = 42):
        """[activity_chain, true_OD_matrix, trips, land_use]"""
        self.raw_data = pd.read_csv(data_path)
        self.batch_size = batch_size
        self.seed = seed
        self.set_setting()
        train_data, val_data, test_data = self._split_data(data=self.raw_data,
                                                           train_percent=train_percent, 
                                                           val_percent=val_percent,
                                                           test_percent=test_percent)
        self.train_dataset, self.val_dataset, self.test_dataset = self._make_datasets(train_data=train_data,
                                                                                      val_data=val_data,
                                                                                      test_data=test_data)
    
    def set_setting(self):
        pass
    
    def fit(self):
        self.train_data, self.val_data, self.test_data = self._make_dataloader(self.train_dataset,
                                                                               self.val_dataset,
                                                                               self.test_dataset)
        return self.train_data, self.val_data, self.test_data

    def _split_data(self, data: pd.DataFrame, 
                    train_percent:float, 
                    val_percent:float, 
                    test_percent:float=None) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, bool]:
        """
        Splits the data into training, validation, and testing sets.

        Parameters:
            train_percent (float): The percentage of data to be used for training.
            val_percent (float): The percentage of data to be used for validation.
            test_percent (float): The percentage of data to be used for testing.

        Returns:
            tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]: A tuple containing the training, validation, and testing
            dataframes.
        """
        train_data, val_test_data = train_test_split(data, train_size=train_percent,
                                                     random_state=self.seed)
        val_data, test_data = train_test_split(val_test_data, train_size=val_percent / (val_percent + test_percent),
                                               random_state=self.seed)
        return train_data, val_data, test_data
    
    def _make_datasets(self, 
                       train_data:pd.DataFrame, 
                       val_data:pd.DataFrame, 
                       test_data:pd.DataFrame) -> tuple[Dataset, Dataset, Dataset]:
        """
        Generates the datasets for training, validation, and testing.

        Args:
            train_data (np.ndarray): The training data.
            val_data (np.ndarray): The validation data.
            test_data (np.ndarray): The testing data.

        Returns:
            tuple: A tuple containing the train dataset, val dataset, and test dataset.
        """
        train_dataset = MyDataset(data=train_data)
        val_dataset = MyDataset(data=val_data)
        test_dataset = MyDataset(data=test_data)                                     

        return train_dataset, val_dataset, test_dataset

    def _make_dataloader(self,
                         train_dataset: MyDataset, 
                         val_dataset: Dataset, 
                         test_dataset: Dataset) -> tuple[DataLoader, DataLoader, DataLoader]:
        """
        Create dataloaders for the given datasets.

        Parameters:
            train_dataset (Dataset): The training dataset.
            val_dataset (Dataset): The validation dataset.
            test_dataset (Dataset): The testing dataset.

        Returns:
            tuple: A tuple containing train_dataloader, val_dataloader, and test_dataloader.
        """
        train_dataloader = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=False, drop_last=True)
        val_dataloader = DataLoader(val_dataset, batch_size=self.batch_size, shuffle=False, drop_last=True)
        test_dataloader = DataLoader(test_dataset, batch_size=self.batch_size, shuffle=False, drop_last=True)
        return train_dataloader, val_dataloader, test_dataloader
