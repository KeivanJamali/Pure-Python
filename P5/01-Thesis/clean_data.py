import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

class Data_Loader:
    def __init__(self, data_list: list):
        """[people_data, family_data, trips_data]"""
        self.data_list = data_list

    def set_setting(self):
        merged_data = self.data_list[2].merge(self.data_list[0],
                                              on=['questionnaire_code', 'person_number'],
                                              how='left')
        merged_data = merged_data.merge(self.data_list[1],
                                        on=['questionnaire_code'],
                                        how='left')
        merged_data = merged_data.drop(columns=['home_area_code_x', 'home_region_code_x','home_area_code_y', 'home_region_code_y'], errors='ignore')
        self.raw_data = merged_data
        