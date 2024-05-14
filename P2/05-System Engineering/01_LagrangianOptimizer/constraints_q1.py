import numpy as np


def constraint_function1(x_s):
    x = x_s[:4]
    return 1000 - (0.3 * x[0] + 0.3 * x[1] + 0.25 * x[2] + 0.15 * x[3])


def constraint_function2(x_s):
    x = x_s[:4]
    return 1000 - (0.25 * x[0] + 0.35 * x[1] + 0.3 * x[2] + 0.1 * x[3])


def constraint_function3(x_s):
    x = x_s[:4]
    return 1000 - (0.45 * x[0] + 0.5 * x[1] + 0.4 * x[2] + 0.22 * x[3])


def constraint_function4(x_s):
    x = x_s[:4]
    return 1000 - (0.15 * x[0] + 0.15 * x[1] + 0.1 * x[2] + 0.05 * x[3])


def constraint_function5(x_s):
    x = x_s[:4]
    s = x_s[4:]
    return x[0] + s[0] - 800


def constraint_function6(x_s):
    x = x_s[:4]
    s = x_s[4:]
    return x[1] + s[1] - 750


def constraint_function7(x_s):
    x = x_s[:4]
    s = x_s[4:]
    return x[2] + s[2] - 600


def constraint_function8(x_s):
    x = x_s[:4]
    s = x_s[4:]
    return x[3] + s[3] - 500


def constraint_function9(x_s):
    x = x_s[:4]
    return np.min(x)


def constraint_function10(x_s):
    s = x_s[4:]
    return np.min(s)


constraints = [constraint_function1, constraint_function2, constraint_function3, constraint_function4,
               constraint_function5, constraint_function6, constraint_function7, constraint_function8,
               constraint_function9, constraint_function10]

types = ["ineq", "ineq", "ineq", "ineq", "eq", "eq", "eq", "eq", "ineq", "ineq"]