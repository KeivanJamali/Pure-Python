import numpy as np
from tabulate import tabulate
import pandas as pd
from copy import deepcopy
import matplotlib.pyplot as plt


class Me_Plot:
    def __init__(self, node_lists: list, title: str, decimal: int = 1, font_size: int = 10):
        self.nodes = sorted(node_lists, key=lambda x: x[0])
        self.decimal = decimal
        self.font_size = font_size
        self.title = title
        self.x = None
        self.y = None
        self._make_x_y()
        self._plot_curve()

    def _make_x_y(self):
        self.x = []
        self.y = []

        for x, y in self.nodes:
            self.x.append(x)
            self.y.append(y)

    def _plot_curve(self):
        plt.plot(self.x, self.y, marker='o', linestyle='-')
        for i, (x, y) in enumerate(zip(self.x, self.y)):
            plt.text(x, y, f'({x:.{self.decimal}f},{y:.{self.decimal}f})', fontsize=self.font_size, ha='right')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(self.title)
        plt.grid(True)
        plt.show()


class Constraint:
    def __init__(self, constraints: list, equality: list) -> None:
        """
        Initialize the class with the given constraints and equality lists.

        Parameters:
            constraints (list): A list of constraints.
            equality (list): A list of equalities.

        Returns:
            None
        """
        self.cons_data = constraints
        self.equality = equality
        self.objective_addition = []
        self.basic_variables_at_first = []
        self.minus_w = [0 for _ in range(len(constraints[0]))]
        self.slack = 0
        self.artificial = 0
        self.excess = 0
        self.label = []
        for i in range(len(self.cons_data)):
            self.check_constraints(i)
        self.constraints = deepcopy(self.cons_data)

    def check_constraints(self, number: int) -> None:
        """
        Check the constraints based on the given number.

        Parameters:
            number (int): The number to check.

        Returns:
            None
        """
        if self.equality[number] == "eq":
            self.add_artificial(number)
        elif self.equality[number] == "ineq" and self.cons_data[number][0] < 0:
            self.add_excess_artificial(number)
        elif self.equality[number] == "ineq" and self.cons_data[number][0] > 0:
            self.add_slack(number)

    def add_slack(self, number: int) -> None:
        """
        Add a slack variable to the constraint matrix for the specified number.

        Parameters:
            number (int): The index at which the slack variable should be added.

        Returns:
            None
        """
        for i in range(len(self.cons_data)):
            if i == number:
                self.cons_data[i].append(1.)
            else:
                self.cons_data[i].append(0.)
        self.objective_addition.append(0.)
        self.minus_w.append(0.)
        self.slack += 1
        self.label.append(f"s{self.slack}")
        self.basic_variables_at_first.append(f"s{self.slack}")

    def add_artificial(self, number: int) -> None:
        """
        Method to add an artificial variable to the linear program.

        Parameters:
            number (int): The index of the artificial variable to be added.

        Returns:
            None
        """
        for i in range(len(self.cons_data)):
            if i == number:
                self.cons_data[i].append(1.)
            else:
                self.cons_data[i].append(0.)
        self.objective_addition.append(0.)
        self.minus_w.append(-1.)
        self.artificial += 1
        self.label.append(f"y{self.artificial}")
        self.basic_variables_at_first.append(f"y{self.artificial}")

    def add_excess_artificial(self, number: int) -> None:
        """
        Add excess artificial variables to the constraint data for a given number.
        :param number: An integer representing the position to add excess artificial variables.
        :return: None
        """
        for i in range(len(self.cons_data)):
            if i == number:
                self.cons_data[i].extend([1., -1.])
            else:
                self.cons_data[i].extend([0., 0.])
        self.objective_addition.extend([0., 0.])
        self.minus_w.extend([0., -1.])
        self.excess += 1
        self.artificial += 1
        self.label.append(f"e{self.excess}")
        self.label.append(f"y{self.artificial}")
        self.basic_variables_at_first.append(f"y{self.artificial}")


class Simplex:
    def __init__(self, objective_function: list, mode: str, parameters: list, decimal: int = 1) -> None:
        """
        Initialize the Simplex class with the given objective function, mode, parameters, and optional decimal value.

        Parameters:
            objective_function (list): The coefficients of the objective function.
            mode (str): The mode of optimization, either 'min' for minimization or 'max' for maximization.
            parameters (list): The parameters of the optimization.
            decimal (int, optional): The number of decimal places to round results to. Defaults to 1.

        Raises:
            ValueError: If the mode is not 'min' or 'max'.
        """
        self.basic_variables_at_first = None
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
        self.result = None
        self.final_table = None
        self.columns = ["Current Values"]
        if mode == "min":
            self.objective_function = [-i for i in self.objective_function]
        elif mode == "max":
            pass
        else:
            raise ValueError("mode must be 'min' or 'max'")

    def fit(self, constraints: Constraint) -> None:
        """
        A method to fit the constraints to the model and perform optimization.
        """
        self.constraints_object = constraints
        self.constraints = np.array(constraints.constraints)
        self.objective_function.extend(constraints.objective_addition)
        self.objective_function = np.array(self.objective_function)
        self.minus_w = constraints.minus_w
        self.minus_w = np.array(self.minus_w)
        self.basic_variables_at_first = constraints.basic_variables_at_first
        self.slack = [f"s{i}" for i in range(1, constraints.slack + 1)]
        self.artificial = [f"y{i}" for i in range(1, constraints.artificial + 1)]
        self.error = [f"e{i}" for i in range(1, constraints.excess + 1)]
        self.label = constraints.label
        self.columns = self.columns + self.parameters + self.label
        self.iteration = 1
        es = [f"e{i}" for i in range(1, constraints.excess + 1)]
        for e in es:
            self.label.remove(e)

        if "y1" in self.label:
            print("[INFO] Two phase solution")
            self.two_phase = True
            self.two_phase_done = False
        else:
            print("[INFO] One phase solution")
            self.two_phase = False
            self.two_phase_done = True

        self._save_data(self.label, self.constraints)

        if self.two_phase:
            print("[INFO] Phase I")
            self._transform_two_phase()
            self._save_data(self.label, self.constraints)
            while not self._check_phase_two():
                self._transform()
                self._save_data(self.label, self.constraints)
            print("[INFO] Phase II Starts.")
            # don't remove artificial variables. If you want to remove change this to code.
            # self._remove_two_phase()
            self.two_phase_done = True
            self._save_data(self.label, self.constraints)
        while not self._check_optimization():
            self._transform()
            self._save_data(self.label, self.constraints)

        self.data.set_index("Basic Variables", inplace=True)
        self._make_result_table()
        self.final_table = self.data.iloc[-(len(self.label) + 2):-1, :]

    def _find_pivot_column(self) -> int:
        """
        Find the pivot column in the objective function and return its index.
        """
        return self.objective_function[1:].argmax(axis=0) + 1

    def _find_pivot_column_two_phase(self) -> int:
        """
        Find the pivot column in the two-phase algorithm.
        No parameters.
        Returns:
            int: The index of the pivot column.
        """
        return self.minus_w[1:].argmax(axis=0) + 1

    def _find_pivot_row(self, column: int) -> int:
        """
        Find the pivot row based on the specified column.

        Parameters:
            column (int): The index of the column to consider.

        Returns:
            int: The index of the pivot row.
        """
        temp = self.constraints[:, column]
        temp[temp == 0] = 0.0000000001
        temp = self.constraints[:, 0] / temp
        temp[temp < 0] = np.inf

        return temp.argmin(axis=0)

    def _find_pivot_element(self) -> tuple:
        """
        A function to find the pivot element in a matrix for optimization problems.
        Returns a tuple containing the pivot element value, row index, and column index.
        """
        column = self._find_pivot_column() if self.two_phase_done else self._find_pivot_column_two_phase()
        row = self._find_pivot_row(column)
        return self.constraints[row][column], row, column

    def _transform(self) -> None:
        """
        Find the pivot element in the constraints matrix and perform row operations to transform the matrix.
        """
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
                if self.two_phase and not self.two_phase_done:
                    temp = self.minus_w[col] / self.constraints[row, col]
                    for j in range(len(self.minus_w)):
                        self.minus_w[j] = self.minus_w[j] - temp * self.constraints[row, j]

        self.label[row] = self.columns[col]

    def _transform_two_phase(self) -> None:
        """
        Transform the two-phase method by identifying rows and columns with specific conditions.
        """
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

    def _remove_two_phase(self) -> None:
        """
        Remove the columns associated with the two-phase method from the model.
        """
        column_num = []
        for l_ in range(len(self.columns)):
            if self.columns[l_][0] == "y":
                column_num.append(l_)
        self.constraints_phase_i = self.constraints.copy()
        self.constraints = np.delete(self.constraints, column_num, axis=1)
        self.objective_function = np.delete(self.objective_function, column_num, axis=0)
        self.columns = [self.columns[i] for i in range(len(self.columns)) if i not in column_num]

    def _check_optimization(self) -> bool:
        """
        Check if the optimization is successful based on the objective function values.

        Parameters:
            None

        Returns:
            bool: True if optimization is successful, False otherwise.
        """
        if self.objective_function[1:].max(axis=0) > 0.0001:
            return False
        else:
            print("[INFO] done!")
            return True

    def _check_phase_two(self) -> bool:
        """
        A function to check phase two with specific conditions and return a boolean value.
        """
        if self.minus_w[0] < 0.001 and self.minus_w[1:].max(axis=0) < 0.0001:
            return True
        else:
            print("[INFO] Infeasible.")
            return False

    def _save_data(self, labels: list, values: np.array) -> None:
        """
        Save data to a DataFrame and update self.data with the new data.

        Args:
            labels (list): Labels for the data.
            values (np.array): Values to be saved in the DataFrame.
        """
        number_of_dash = 20
        data = pd.DataFrame(values, columns=self.columns)
        data["Basic Variables"] = labels
        data_z = pd.DataFrame([self.objective_function], columns=self.columns)
        data_z["Basic Variables"] = f"-z{self.iteration}"
        if self.two_phase and not self.two_phase_done:
            data_w = pd.DataFrame([self.minus_w], columns=self.columns)
            data_w["Basic Variables"] = f"-w{self.iteration}"

        data_empty = pd.DataFrame([np.array([f"{number_of_dash * "-"}" for _ in range(len(self.columns))])],
                                  columns=self.columns)
        data_empty["Basic Variables"] = f"{number_of_dash * "-"}"

        self.iteration += 1

        if self.two_phase and not self.two_phase_done:
            data = pd.concat((data, data_z, data_w, data_empty), ignore_index=True)
        else:
            data = pd.concat((data, data_z, data_empty), ignore_index=True)

        if self.data is not None:
            self.data = pd.concat((self.data, data), ignore_index=True)
        else:
            self.data = data

    def make_table(self, format_: str) -> None:
        """
        A function to generate a table in a specified format.

        Parameters:
            format_ (str): The format of the table. It can be "github", "latex", or "excel".

        Returns:
            None if the format is not supported, otherwise it prints a table in the specified format.
        """
        if format_ not in ["github", "latex", "excel"]:
            return None
        print(tabulate(self.data, headers="keys", tablefmt=format_, numalign="right", floatfmt=f".{self.decimal}f"))

    def _make_result_table(self) -> None:
        """
        Generates a result table based on the columns and data attributes of the object.
        Updates the 'result' attribute with the computed values.
        Prints the result table using the tabulate library with specified formatting options.
        """
        result = {}
        for l_ in self.columns:
            if l_ not in self.label:
                result[l_] = 0
            else:
                result[l_] = self.data[self.data.index == l_].iloc[-1, 0]
        result["Current Values"] = -self.data.iloc[-2, 0]
        self.result = pd.DataFrame(result, index=[0])
        print(tabulate(self.result, headers="keys", tablefmt="github", numalign="right", floatfmt=f".{self.decimal}f"))


class Sensitivity_Analysis:
    def __init__(self, table: Simplex):
        self.teta = None
        self.righthand = None
        self.righthand_b = None
        self.shadow_prices = {}
        self.righthand_nodes = []
        self.coefficient_nodes = []
        self.tabulate = table.final_table.copy()
        self.basic_variables_at_first = table.basic_variables_at_first.copy()
        self._set_setting()
        self.make_shadow_prices()

    def _set_setting(self):
        self.label = list(self.tabulate.index)
        self.columns = list(self.tabulate.columns[:])
        self.constraints = self.tabulate.iloc[:-1, :].values.copy()
        self.objective_function = self.tabulate.iloc[-1, :].values.copy()

    def make_shadow_prices(self):
        for c in range(len(self.columns[1:])):
            temp = -self.tabulate.iloc[-1, c + 1]
            self.shadow_prices[self.columns[1:][c]] = 0 if abs(temp) < 0.001 else temp

    def change_coefficient(self):
        pass

    def change_righthand(self, righthands_at_first: list = None, righthands_at_last: list = None):
        if righthands_at_first and not righthands_at_last:
            self.righthand_b = self._from_first_to_final(righthand=righthands_at_first).copy()
        elif not righthands_at_first and righthands_at_last:
            self.righthand_b = righthands_at_last.copy()
        else:
            print("[ERROR]")

        self.righthand = self.righthand_b.copy()
        if len(self.righthand) != len(self.label):
            raise ValueError("number of righhands must be equal to the number of rows.")

        self.teta = 0
        self.righthand_nodes.append([self.teta, -(self.objective_function[0] + self.teta * self.righthand[-1])])

        self._set_setting()
        while abs(self.objective_function[0] + self.teta * self.righthand[-1]) > 0.0001:
            self._transform(mode="d")
            self.righthand_nodes.append([self.teta, -(self.objective_function[0] + self.teta * self.righthand[-1])])
            if abs(self.righthand[-1]) < 0.01:
                break

        self._set_setting()
        self.righthand = self.righthand_b.copy()
        self.teta = 0
        while abs(self.objective_function[0] + self.teta * self.righthand[-1]) > 0.0001:
            self._transform(mode="u")
            self.righthand_nodes.append([self.teta, -(self.objective_function[0] + self.teta * self.righthand[-1])])
            if abs(self.righthand[-1]) < 0.01:
                break

        Me_Plot(self.righthand_nodes, title="Righthand limits")

    def _find_pivot_row_righthand(self, mode: str) -> int:
        temp = []
        for i in range(len(self.constraints[:, 0])):
            if abs(self.righthand[i]) > 0.001:
                temp.append(-self.constraints[i, 0] / self.righthand[i])
            else:
                temp.append(0)
        if mode == "u":
            row = np.argmax(temp)
            self.teta = np.max(temp)
        elif mode == "d":
            row = np.argmin(temp)
            self.teta = np.min(temp)
        return row

    def _find_pivot_column_righthand(self, row) -> int:
        temp = []
        for i in range(1, len(self.constraints[row, :])):
            temp2 = 0.0001 if self.constraints[row, i] == 0 else self.constraints[row, i]
            temp.append(self.objective_function[i] / temp2)
        temp = np.array(temp)
        temp[temp < 0.001] = np.inf
        column = np.argmin(temp)
        return column + 1

    def _find_pivot_element_righthand(self, mode: str) -> tuple:
        row = self._find_pivot_row_righthand(mode=mode)
        column = self._find_pivot_column_righthand(row)
        return self.constraints[row][column], row, column

    def _transform(self, mode: str) -> None:
        element, row, col = self._find_pivot_element_righthand(mode=mode)
        for i in range(len(self.constraints)):
            if i == row:
                self.constraints[i, :] = self.constraints[i, :] / element
                self.righthand[row] = self.righthand[row] / element
            else:
                temp = self.constraints[i, col] / self.constraints[row, col]
                for j in range(len(self.constraints[0, :])):
                    self.constraints[i, j] = self.constraints[i, j] - temp * self.constraints[row, j]
                self.righthand[i] = self.righthand[i] - temp * self.righthand[row]

        temp = self.objective_function[col] / self.constraints[row, col]
        for j in range(len(self.objective_function)):
            self.objective_function[j] = self.objective_function[j] - temp * self.constraints[row, j]
        self.righthand[-1] = self.righthand[-1] - temp * self.righthand[row]

        self.label[row] = self.columns[col]

    def _from_first_to_final(self, righthand):
        new_righthand = []
        columns = []
        for n in self.basic_variables_at_first:
            for j in range(len(self.columns)):
                if n == self.columns[j]:
                    columns.append(j)
                    break

        for i in range(len(righthand) - 1):
            temp = 0
            for j in range(len(righthand) - 1):
                temp += righthand[j] * self.constraints[i, columns[j]]
            new_righthand.append(temp)

        temp = 0
        for j in range(len(righthand) - 1):
            temp += righthand[j] * self.objective_function[columns[j]]
        new_righthand.append(temp)

        return new_righthand
