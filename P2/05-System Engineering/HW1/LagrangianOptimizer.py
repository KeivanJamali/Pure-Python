import numpy as np
from scipy.optimize import minimize
from tabulate import tabulate


class LagrangianOptimizer:
    def __init__(self, number_of_parameter):
        """
        Initialize the class with the given number_of_parameter.

        Parameters:
            number_of_parameter (int): The number of parameters to initialize the class with.

        Returns:
            None
        """
        self.number_of_parameters = number_of_parameter
        self.bound = []
        self.constraints = []
        self.result = None

    def _initial_value(self):
        """
        Generates an initial value for the parameters using numpy's random number generator.
        Returns the initial parameter values as an array.
        """
        x = np.random.randint(0, 100, size=self.number_of_parameters)
        return x

    def set_boundaries(self, lower_boundaries: list, upper_boundaries: list):
        """
        Sets the boundaries for the given parameters. In this case 'None' means no boundary.
        example:
            [0, None]
            [None, None]
            means that (0, +inf) and (-inf, +inf) are the boundaries

        :param lower_boundaries: A list of lower boundaries
        :param upper_boundaries: A list of upper boundaries
        :return: None
        """
        for i in range(len(lower_boundaries)):
            self.bound.append((lower_boundaries[i], upper_boundaries[i]))

    def build_constrains(self, types: list, constraints: list):
        """
        Build constraints based on the given type list.

        Parameters:
            types (list): The list of types for the constraints(eq or ineq).
            constraints: The list of constraints.

        Returns:
            tuple: A tuple of dictionaries representing the constraints.
        """
        for i in range(len(constraints)):
            self.constraints.append({"type": types[i], "fun": constraints[i]})

        self.constraints = tuple(self.constraints)

    def optimize(self, objective_function: callable, method: str):
        """
        Optimize the objective function using the specified method.

        :param objective_function: The objective function to be minimized.
        :param method: The optimization method to be used ('SLSQP' or 'COBYLA').
        :return: The result of the optimization.
        """
        if method == "COBYLA":
            options = {"maxiter": 1000, "disp": True}
            self.result = minimize(objective_function, self._initial_value(), method=method, bounds=self.bound,
                                   constraints=self.constraints, options=options)
        elif method == "SLSQP":
            self.result = minimize(objective_function, self._initial_value(), method=method, bounds=self.bound,
                                   constraints=self.constraints)
        return self.result

    def result_table(self, parameters: list = None):
        """
        Generate a table with the parameters and their corresponding values, using self.result.x and self.result.fun.
        The table is printed using the tabulate function with the "github" table format.
        """
        data = [["Parameters", "Value"]]
        for i in range(len(self.result.x)):
            if parameters:
                data.append([parameters[i], self.result.x[i]])
            else:
                data.append([f"x{i + 1}", self.result.x[i]])
        data.append(["Optimal value", abs(self.result.fun)])
        print(tabulate(data, headers="firstrow", tablefmt="github", numalign="right"))
