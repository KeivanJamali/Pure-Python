import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import Dataset, DataLoader
import torch
import Information as info
from ast import literal_eval


class MyDataset(Dataset):
    def __init__(self, data: pd.DataFrame, dynamic_features: list, static_features: list, target_col, seq_len=10):
        """
        Initializes a new instance of the class.

        Args:
            data (pd.DataFrame): The data to be used for initialization.

        Returns:
            None
        """
        self.data = data
        self.dynamic_features = dynamic_features
        self.target_col = target_col
        self.static_features = static_features
        self.seq_len = seq_len

        self.X, self.y = self._build_sequences()

    def _build_sequences(self):
        X_list, y_list = [], []
        for _, row in self.data.iterrows():
            seq_data = []
            for feat in self.dynamic_features:
                val = row[feat]
                if isinstance(val, list):
                    seq_data.append(val[:self.seq_len] + [0]*(self.seq_len - len(val)))
                else:
                    seq_data.append([val]*self.seq_len)

            seq_data = np.stack(seq_data, axis=-1)  # shape: [seq_len, num_features]
            X_list.append(seq_data)
            y_list.append(row[self.target_col])
        
        static = self.data[self.static_features].values

        return [np.array(X_list, dtype=np.float32), static], np.array(y_list, dtype=np.int64)

    def __len__(self):
        """You most probably need to change the slices."""
        return len(self.data)

    def __getitem__(self, idx):
        """You most probably need to change the slices. returns x1, x2, y"""
        return torch.tensor(self.X[0][idx], dtype=torch.float), torch.tensor(self.X[1][idx], dtype=torch.float), torch.tensor(self.y[idx], dtype=torch.long)


class MyDataloader:
    def __init__(self, data_list:list, seed=42):
        """[activity_chain, true_OD_matrix, trips]"""
        self.raw_data_activity = data_list[0]
        self.raw_data_true_od = data_list[1]
        self.raw_data_trips = data_list[2]
        self.seed = seed
        self.scalers = {}
        self.set_setting()
    
    def set_setting(self):
        data_activity = self.raw_data_activity.copy()

        drop_cols = ['Unnamed: 0', 'family_id']
        data_activity.drop(columns=[c for c in drop_cols if c in data_activity.columns], inplace=True)

        # We saw that the data 14075 has trip mode of [nan, nan]. also data 36942 [nan, nan]. remove theses two rows.
        data_activity.drop([14075, 36942], inplace=True, axis=0)
        data_activity.reset_index(drop=True, inplace=True)

        list_cols = ["activity_chain", "time_chain", "purpose_chain", "area_zones", "region_zones", "duration", "travel_mode", "trip_distance", "hourly_correction_factor"]
        for col in list_cols:
            if col in data_activity.columns and data_activity[col].dtype == object:
                data_activity[col] = data_activity[col].apply(lambda x: literal_eval(str(x)) if pd.notna(x) else [])

        # Define dynamic (sequence) and static features
        self.dynamic_features = ['activity_chain', 'time_chain', 'purpose_chain', 'trip_distance', 'travel_mode']
        self.static_features = [
            'gender', 'age', 'job', 'working', 'driving_license', 'education_level',
            'home_area_code', 'home_region_code', 'family_members_count', 'total_vehicles_count',
            'bicycles_24inch_or_larger_count', 'motorcycles_count', 'private_cars_count',
            'pickup_trucks_count', 'taxis_count', 'other_vehicles_count'
        ]
        self.target_column = ""

        self.data_activity = data_activity

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
        if test_percent:
            val_data, test_data = train_test_split(val_test_data, train_size=val_percent / (val_percent + test_percent),
                                                   random_state=self.seed)
            return train_data, val_data, test_data, True
        else:
            return train_data, val_test_data, None, False

    def _scale_data(self, train_data, val_data, test_data, have_test):
        """
        Scale numeric/static features
        """
        train_scaled, val_scaled, test_scaled = train_data.copy(), val_data.copy(), None

        # Standard scale continuous variables
        num_cols = ['age', 'trip_distance', 'duration', "private_car_1", "private_car_2", "private_car_3", "private_car_4"]
        for col in num_cols:
            if col in train_data.columns:
                scaler = StandardScaler()
                train_scaled[col] = scaler.fit_transform(train_data[[col]])
                val_scaled[col] = scaler.transform(val_data[[col]])
                if have_test:
                    test_scaled = test_data.copy()
                    test_scaled[col] = scaler.transform(test_data[[col]])
                self.scalers[col] = scaler

        return train_scaled, val_scaled, test_scaled
    
    def _scale_data(self, 
                    train_data:pd.DataFrame, 
                    val_data:pd.DataFrame, 
                    test_data:pd.DataFrame, 
                    have_test:bool) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Scale the data data using MinMaxScaler.

        Parameters:
            train_data (pd.DataFrame): The training data.
            val_data (pd.DataFrame): The validation data.
            test_data (pd.DataFrame): The test data.

        Returns:
            tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]: The scaled training, validation, and test data.
        """
        self.scaler_x = StandardScaler()
        cols = ["age"]
        train_data[cols] = self.scaler_x.fit_transform(train_data[cols])
        val_data[cols] = self.scaler_x.transform(val_data[cols])
        if have_test:
            test_data[cols] = self.scaler_x.transform(test_data[cols])
        return train_data, val_data, test_data
    
    def _make_datasets(self, 
                       train_data:pd.DataFrame, 
                       val_data:pd.DataFrame, 
                       test_data:pd.DataFrame, 
                       have_test:pd.DataFrame) -> tuple[Dataset, Dataset, Dataset]:
        """
        Generates the datasets for training, validation, and testing.

        Args:
            train_data (np.ndarray): The training data.
            val_data (np.ndarray): The validation data.
            test_data (np.ndarray): The testing data.

        Returns:
            tuple: A tuple containing the train dataset, val dataset, and test dataset.
        """
        train_dataset = MyDataset(train_data, dynamic_features=self.dynamic_features, static_features=self.static_features, target_col=)
        val_dataset = MyDataset(val_data)
        if have_test:
            test_dataset = MyDataset(test_data)
            return train_dataset, val_dataset, test_dataset
        else:
            return train_dataset, val_dataset, None

    def _make_dataloader(self, train_dataset: MyDataset, 
                         val_dataset: MyDataset, 
                         test_dataset: MyDataset) -> tuple[DataLoader, DataLoader, DataLoader]:
        """
        Create dataloaders for the given datasets.

        Parameters:
            train_dataset (Dataset): The training dataset.
            val_dataset (Dataset): The validation dataset.
            test_dataset (Dataset): The testing dataset.

        Returns:
            tuple: A tuple containing train_dataloader, val_dataloader, and test_dataloader.
        """
        train_dataloader = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=False, drop_last=False)
        val_dataloader = DataLoader(val_dataset, batch_size=self.batch_size, shuffle=False, drop_last=False)
        test_dataloader = DataLoader(test_dataset, batch_size=self.batch_size, shuffle=False, drop_last=False)
        return train_dataloader, val_dataloader, test_dataloader
