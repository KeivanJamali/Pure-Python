import numpy as np


def constraint_function1(x):
    x_a = x[:4]
    x_b = x[4:8]
    r = x[8:]
    return x_a[0] + x_b[0] + r[0] - 10000


def constraint_function2(x):
    x_a = x[:4]
    x_b = x[4:8]
    r = x[8:]
    return x_a[1] + x_b[1] + r[1] - r[0]


def constraint_function3(x):
    x_a = x[:4]
    x_b = x[4:8]
    r = x[8:]
    return -1.4 * x_a[0] + x_a[2] + x_b[2] + r[2] - r[1]


def constraint_function4(x):
    x_a = x[:4]
    x_b = x[4:8]
    r = x[8:]
    return -1.7 * x_b[0] - 1.4 * x_a[1] + x_a[3] + x_b[3] + r[3] - r[2]


constraints = [constraint_function1, constraint_function2, constraint_function3, constraint_function4]

types = ["eq", "eq", "eq", "eq"]
