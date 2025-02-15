import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment
from tabulate import tabulate

class Defind_Problem:
    def __init__(self, feature1, feature2):
        self.data_initial = pd.DataFrame(0, index=feature1, columns=feature2)
        self.data = pd.DataFrame(0, index=feature1, columns=feature2)
        self.empty_data = pd.DataFrame(0, index=feature1, columns=feature2)
        self.resultant_data = None
        self.s = None
        self.n = len(feature1)

    def add_row(self, name, data):
        self.data.loc[name] = data
        self.data_initial.loc[name] = data

    def add_column(self, name, data):
        self.data.loc[:, name] = data
        self.data_initial.loc[:, name] = data

    def change_to_min(self, m):
        self.data = self.data * -1 + m

    def fit(self):
        self.resultant_data = self.data.copy()
        self._step_one()

        while True:
            self._step_two()
            if self._check_optimality():
                zeroes = self._step_four()
                print(f"Total experience is {self.s}")
                return zeroes
            self._step_three()
        

    def _step_one(self):
        min_rows = list(self.resultant_data.min(axis=1))
        self.resultant_data = self.resultant_data.subtract(min_rows, axis=0)
        min_columns = list(self.resultant_data.min(axis=0))
        self.resultant_data = self.resultant_data.subtract(min_columns, axis=1)

        # print(self.resultant_data)

    def _step_two(self):
        self.n_temp = 0
        self.temp = self.resultant_data.copy()
        self.temp2 = self.empty_data.copy()
        while True:
            zeros_total = []
            zeros_row = list(self.temp[self.temp == 0].count(axis=1)) # number of zeros in rows
            zeros_column = list(self.temp[self.temp == 0].count(axis=0)) # number of zeros in columns
            zeros_total.extend(zeros_row)
            zeros_total.extend(zeros_column)
            max_value = max(zeros_total)
            if max_value == 0:
                return True
            try:
                max_index = zeros_row.index(max_value)
                row = True
                column = False
            except:
                max_index = zeros_column.index(max_value)
                row = False
                column = True

            if row:
                self.temp.iloc[max_index, :] = [-1 for _ in range(len(self.temp.index))]
                self.temp2.iloc[max_index, :] += [-1 for _ in range(len(self.temp.index))]
                print(f"one line in row {max_index+1}")
                self.n_temp += 1

            elif column:
                self.temp.iloc[:, max_index] = [-1 for _ in range(len(self.temp.columns))]
                self.temp2.iloc[:, max_index] += [-1 for _ in range(len(self.temp.columns))]
                print(f"one line in column {max_index+1}")
                self.n_temp += 1


    def _check_optimality(self):
        if self.n_temp < self.n:
            return False
        else:
            return True
        
    def _step_three(self):
        self.mask_p = self.temp != -1
        self.mask_n = self.temp2 == -2
        
        k = self.temp[self.mask_p].values.flatten()
        k = pd.Series(k).dropna().min()
        print(k)

        self.resultant_data[self.mask_p] = self.resultant_data[self.mask_p] - k
        self.resultant_data[self.mask_n] = self.resultant_data[self.mask_n] + k
        print(self.resultant_data)

    def _step_four(self):
        data = self.resultant_data.copy()
        # Replace non-zero values with a large number to create a cost matrix
        cost_matrix = data.replace(0, 0).replace([data != 0], np.inf)
        
        # Convert DataFrame to a NumPy array
        cost_matrix = cost_matrix.to_numpy()

        # Apply the Hungarian algorithm to find the optimal assignment
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        # Extract positions of the selected zeros
        zero_positions = [(int(row)+1, int(col)+1) for row, col in zip(row_ind, col_ind)]
        self.s = 0
        for point in zero_positions:
            self.s += self.data_initial.iloc[point[0]-1, point[1]-1]

        return zero_positions

        


        