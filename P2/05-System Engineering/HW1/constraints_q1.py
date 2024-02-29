import numpy as np


def constraint_function1(x):
    return 6 * x[0] + 4 * x[1] - 0.9 * 480


def constraint_function2(x):
    return 5 * x[0] + 5 * x[1] - 0.86 * 480


def constraint_function3(x):
    return 4 * x[0] + 6 * x[1] - 0.88 * 480


def constraint_function4(x):
    return -1267.2 + 15 * (x[0] + x[1])


constraints = [constraint_function1, constraint_function2, constraint_function3, constraint_function4]

types = ["ineq", "ineq", "ineq", "ineq"]
