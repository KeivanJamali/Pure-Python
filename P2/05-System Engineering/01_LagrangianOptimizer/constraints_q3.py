import numpy as np


def constraint_function1(x):
    return 2 * x[1] + 2 * x[2] + 4 * x[3] + x[4] - 150


def constraint_function2(x):
    return x[0] + x[1] + 2 * x[4] - 200


def constraint_function3(x):
    return x[0] + x[2] + 2 * x[5] - 300


constraints = [constraint_function1, constraint_function2, constraint_function3]

types = ["ineq", "ineq", "ineq"]
