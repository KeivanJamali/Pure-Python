import numpy as np
from tabulate import tabulate
import pandas as pd
from copy import deepcopy


class Constraint:
    def __init__(self, constraints: list, equality: list):
        self.cons_data = constraints
        self.equality = equality
        self.objective_addition = []
        self.minus_w = [0 for _ in range(len(constraints[0]))]
        self.slack = 0
        self.artificial = 0
        self.error = 0
        self.label = []
        for i in range(len(self.cons_data)):
            self.check_constraints(i)
        self.constraints = deepcopy(self.cons_data)

    def check_constraints(self, number: int) -> None:
        if self.equality[number] == "eq":
            self.add_artificial(number)
        elif self.equality[number] == "ineq" and self.cons_data[number][0] < 0:
            self.add_error_artificial(number)
        elif self.equality[number] == "ineq" and self.cons_data[number][0] > 0:
            self.add_slack(number)

    def add_slack(self, number: int):
        for i in range(len(self.cons_data)):
            if i == number:
                self.cons_data[i].append(1.)
            else:
                self.cons_data[i].append(0.)
        self.objective_addition.append(0.)
        self.minus_w.append(0.)
        self.slack += 1
        self.label.append(f"s{self.slack}")

    def add_artificial(self, number: int):
        for i in range(len(self.cons_data)):
            if i == number:
                self.cons_data[i].append(1.)
            else:
                self.cons_data[i].append(0.)
        self.objective_addition.append(0.)
        self.minus_w.append(-1.)
        self.artificial += 1
        self.label.append(f"y{self.artificial}")

    def add_error_artificial(self, number: int):
        for i in range(len(self.cons_data)):
            if i == number:
                self.cons_data[i].extend([1., -1.])
            else:
                self.cons_data[i].extend([0., 0.])
        self.objective_addition.extend([0., 0.])
        self.minus_w.extend([0., -1.])
        self.error += 1
        self.artificial += 1
        self.label.append(f"e{self.error}")
        self.label.append(f"y{self.artificial}")


class Simplex:
    def __init__(self, objective_function: list, parameters: list, decimal: int = 1):
        self.two_phase = None
        self.two_phase_done = None
        self.objective_function = objective_function
        self.minus_w = None
        self.parameters = parameters
        self.number_of_parameters = len(parameters)
        self.decimal = decimal
        self.constraints = None
        self.data = None
        self.iteration = None
        self.slack = None
        self.artificial = None
        self.error = None
        self.label = None
        self.constraints_object = None
        self.columns = ["Current Values"]

    def fit(self, constraints: Constraint):
        self.constraints_object = constraints
        self.constraints = np.array(constraints.constraints)
        self.objective_function.extend(constraints.objective_addition)
        self.objective_function = np.array(self.objective_function)
        self.minus_w = constraints.minus_w
        self.minus_w = np.array(self.minus_w)
        self.slack = [f"s{i}" for i in range(1, constraints.slack + 1)]
        self.artificial = [f"y{i}" for i in range(1, constraints.artificial + 1)]
        self.error = [f"e{i}" for i in range(1, constraints.error + 1)]
        self.label = constraints.label
        self.columns = self.columns + self.parameters + self.label
        self.iteration = 1
        es = [f"e{i}" for i in range(1, constraints.error + 1)]
        for e in es:
            self.label.remove(e)

        if "y1" in self.label:
            print("[INFO] Two phase solution")
            self.two_phase = True
            self.two_phase_done = False
        else:
            print("[INFO] One phase solution")
            self.two_phase = False

        self._save_data(self.label, self.constraints)

        if self.two_phase:
            print("[INFO] Phase I")
            self._transform_two_phase()
            self._save_data(self.label, self.constraints)
            while not self._check_phase_two():
                self._transform()
                self._save_data(self.label, self.constraints)
            print("[INFO] Phase II Starts.")
            self._remove_two_phase()
            self.two_phase_done = True
            self._save_data(self.label, self.constraints)

        while not self._check_optimization():
            self._transform()
            self._save_data(self.label, self.constraints)
        self.data.set_index("Basic Variables", inplace=True)
        self._make_result_table()

    def _find_pivot_column(self) -> int:
        return self.objective_function[1:].argmax(axis=0) + 1

    def _find_pivot_column_two_phase(self) -> int:
        return self.minus_w[1:].argmax(axis=0) + 1

    def _find_pivot_row(self, column: int) -> int:
        temp = self.constraints[:, column]
        temp[temp == 0] = 0.0000000001
        temp = self.constraints[:, 0] / temp
        temp[temp < 0] = np.inf
        return temp.argmin(axis=0)

    def _find_pivot_element(self) -> tuple:
        column = self._find_pivot_column() if not self.two_phase else self._find_pivot_column_two_phase()
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
                if self.two_phase:
                    temp = self.minus_w[col] / self.constraints[row, col]
                    for j in range(len(self.minus_w)):
                        self.minus_w[j] = self.minus_w[j] - temp * self.constraints[row, j]

        self.label[row] = self.columns[col]

    def _transform_two_phase(self):
        rows_num = []
        columns_num = []

        for i in range(len(self.columns)):
            if self.columns[i][0] == "y":
                columns_num.append(i)

        for i in range(len(self.constraints)):
            for j in columns_num:
                if abs(self.constraints[i][j] - 1) < 0.0001:
                    rows_num.append([i, 1])
                elif abs(self.constraints[i][j] + 1) < 0.0001:
                    rows_num.append([i, -1])

        for i in rows_num:
            self.minus_w = self.minus_w + self.constraints[i[0]] * i[1]

    def _remove_two_phase(self):
        column_num = []
        for l in range(len(self.columns)):
            if self.columns[l][0] == "y":
                column_num.append(l)
        self.constraints_phase_i = self.constraints.copy()
        self.constraints = np.delete(self.constraints, column_num, axis=1)
        self.objective_function = np.delete(self.objective_function, column_num, axis=0)
        self.columns = [self.columns[i] for i in range(len(self.columns)) if i not in column_num]

    def _check_optimization(self) -> bool:
        if self.objective_function[1:].max(axis=0) > 0.0001:
            return False
        else:
            print("done!")
            return True

    def _check_phase_two(self) -> bool:
        ys = [f"y{i}" for i in range(1, self.constraints_object.artificial + 1)]
        if self.minus_w[0] < 0.001:
            for y in ys:
                if y in self.label:
                    return False
            return True
        else:
            return False

    def _save_data(self, labels: list, values: np.array):
        data = pd.DataFrame(values, columns=self.columns)
        data["Basic Variables"] = labels
        data_z = pd.DataFrame([self.objective_function], columns=self.columns)
        data_z["Basic Variables"] = f"-z{self.iteration}"
        if self.two_phase and not self.two_phase_done:
            data_w = pd.DataFrame([self.minus_w], columns=self.columns)
            data_w["Basic Variables"] = f"-w{self.iteration}"

        self.iteration += 1

        if self.two_phase and not self.two_phase_done:
            data = pd.concat((data, data_z, data_w), ignore_index=True)
        else:
            data = pd.concat((data, data_z), ignore_index=True)

        if self.data is not None:
            self.data = pd.concat((self.data, data), ignore_index=True)
        else:
            self.data = data

    def make_table(self, format_: str):
        if format_ not in ["github", "latex", "excel"]:
            return None
        print(tabulate(self.data, headers="keys", tablefmt=format_, numalign="right", floatfmt=f".{self.decimal}f"))

    def _make_result_table(self):
        # len(self.slack) + 1
        result = {}
        for l in self.columns:
            if l not in self.label:
                result[l] = 0
            else:
                result[l] = self.data[self.data.index == l].iloc[-1, 0]
        result["Current Values"] = -self.data.iloc[-1, 0]
        result = pd.DataFrame(result, index=[0])
        print(tabulate(result, headers="keys", tablefmt="github", numalign="right", floatfmt=f".{self.decimal}f"))
