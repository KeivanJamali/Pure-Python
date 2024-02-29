import numpy as np
from tabulate import tabulate
import pandas as pd


class Simplex:
    def __init__(self, objective_function: list, parameters: list, decimal: int = 1):
        self.objective_function = np.array(objective_function)
        self.parameters = parameters
        self.number_of_parameters = len(parameters)
        self.stack = [f"s{i}" for i in range(1, len(self.objective_function) - self.number_of_parameters)]
        self.label = self.stack.copy()
        self.columns = self.parameters + self.stack
        self.columns.append("Optimal value")
        self.constraints = None
        self.data = None
        self.iteration = 1
        self.decimal = decimal

    def fit(self, constraints: list):
        self.constraints = np.array(constraints)
        self._save_data(self.label, self.constraints)

        while not self._check_optimization():
            self._transform()
            self._save_data(self.label, self.constraints)
        self.data.set_index("parameter", inplace=True)
        self._make_result_table()

    def _find_pivot_column(self) -> int:
        return self.objective_function.argmin(axis=0)

    def _find_pivot_row(self, column: int) -> int:
        temp = self.constraints[:, column]
        temp[temp == 0] = 0.0000000001
        temp = self.constraints[:, -1] / temp
        return temp.argmin(axis=0)

    def _find_pivot_element(self) -> tuple:
        column = self._find_pivot_column()
        row = self._find_pivot_row(column)
        return self.constraints[row][column], row, column

    def _transform(self):
        element, row, col = self._find_pivot_element()
        for i in range(len(self.constraints)):
            if i == row:
                self.constraints[i, :] = self.constraints[i, :] / element
            else:
                temp = self.constraints[i, col] / self.constraints[row, col]
                for j in range(len(self.constraints[0, :])):
                    self.constraints[i, j] = self.constraints[i, j] - temp * self.constraints[row, j]
                temp = self.objective_function[col] / self.constraints[row, col]
                for j in range(len(self.objective_function)):
                    self.objective_function[j] = self.objective_function[j] - temp * self.constraints[row, j]

        self.label[row] = self.columns[col]

    def _check_optimization(self) -> bool:
        if self.objective_function.min(axis=0) < 0:
            return False
        else:
            return True

    def _save_data(self, labels: list, values: np.array):
        data = pd.DataFrame(values, columns=self.columns)
        data["parameter"] = labels
        data_z = pd.DataFrame([self.objective_function], columns=self.columns)
        data_z["parameter"] = f"z{self.iteration}"
        self.iteration += 1
        data = pd.concat((data, data_z), ignore_index=True)

        if self.data is not None:
            self.data = pd.concat((self.data, data), ignore_index=True)
        else:
            self.data = data

    def make_table(self):
        print(tabulate(self.data, headers="keys", tablefmt="github", numalign="right", floatfmt=f".{self.decimal}f"))

    def _make_result_table(self):
        len(self.stack) + 1
        result = {}
        for l in self.columns:
            if l not in self.label:
                result[l] = 0
            else:
                result[l] = self.data[self.data.index == l].iloc[-1, -1]
        result["Optimal value"] = self.data.iloc[-1, -1]
        result = pd.DataFrame(result, index=[0])
        print(tabulate(result, headers="keys", tablefmt="github", numalign="right", floatfmt=f".{self.decimal}f"))
