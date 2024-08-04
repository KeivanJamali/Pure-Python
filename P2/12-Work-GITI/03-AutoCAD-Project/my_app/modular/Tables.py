import pandas as pd

file_bal = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\raw_data\Bridges_bal.csv"
file_full = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\raw_data\Bridges_one_full.csv"
file_one = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\raw_data\Bridges_one.csv"

class Tables:
    def __init__(self):
        self.bal_table = pd.read_csv(file_bal)
        self.full_table = pd.read_csv(file_full)
        self.one_table = pd.read_csv(file_one)
        