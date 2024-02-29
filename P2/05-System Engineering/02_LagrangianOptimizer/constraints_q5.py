import numpy as np


def constraint_function1(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return -(y_a[0] * x[0] + y_a[1] * x[1] + y_a[2] * x[2] - 4000)


def constraint_function2(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return -(y_b[0] * x[0] + y_b[1] * x[1] + y_b[2] * x[2] - 5000)


def constraint_function3(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return -(y_c[0] * x[0] + y_c[1] * x[1] + y_c[2] * x[2] - 2500)


def constraint_function4(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return (y_a[0] - 0.6)


def constraint_function5(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return (y_a[1] - 0.15)


def constraint_function6(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return (-y_c[0] + 0.2)


def constraint_function7(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return (-y_c[1] + 0.6)


def constraint_function8(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return (-y_c[2] + 0.5)


def constraint_function9(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return (y_a[0] + y_b[0] + y_c[0] - 1)


def constraint_function10(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return (y_a[1] + y_b[1] + y_c[1] - 1)


def constraint_function11(x_y):
    x = x_y[:3]
    y_a = x_y[3:6]
    y_b = x_y[6:9]
    y_c = x_y[9:12]
    return (y_a[2] + y_b[2] + y_c[2] - 1)


constraints = [constraint_function1, constraint_function2, constraint_function3, constraint_function4,
               constraint_function5, constraint_function6, constraint_function7, constraint_function8,
               constraint_function9, constraint_function10, constraint_function11]

types = ["ineq", "ineq", "ineq", "ineq", "ineq", "ineq", "ineq", "ineq", "eq", "eq", "eq"]
