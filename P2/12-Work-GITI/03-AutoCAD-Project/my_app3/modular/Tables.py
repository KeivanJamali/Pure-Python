import pandas as pd
import os

# Define relative path to the data folder
base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, '..', 'data')

file_dastak = os.path.join(data_dir, 'Culvert_dastak.csv')
file_full = os.path.join(data_dir, 'Culvert_full.csv')
file_one = os.path.join(data_dir, 'Culvert_one.csv')
file_multi = os.path.join(data_dir, 'Culvert_multi.csv')
file_multi_extra = os.path.join(data_dir, 'Culvert_multi_extra.csv')

class Tables:
    def __init__(self):
        """This class will read tables and store them.
        """
        self.dastak_table = pd.read_csv(file_dastak)
        self.full_table = pd.read_csv(file_full)
        self.one_table = pd.read_csv(file_one)
        self.multi_table = pd.read_csv(file_multi)
        self.multi_extra_table = pd.read_csv(file_multi_extra)
        