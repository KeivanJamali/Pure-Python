import pandas as pd
import os

# Define relative path to the data folder
base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, '..', 'data')

file_bal = os.path.join(data_dir, 'Bridges_bal.csv')
file_full = os.path.join(data_dir, 'Bridges_one_full.csv')
file_one = os.path.join(data_dir, 'Bridges_one.csv')

class Tables:
    def __init__(self):
        self.bal_table = pd.read_csv(file_bal)
        self.full_table = pd.read_csv(file_full)
        self.one_table = pd.read_csv(file_one)
        