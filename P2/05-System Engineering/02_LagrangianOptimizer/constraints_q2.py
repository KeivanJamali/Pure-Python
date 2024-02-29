import numpy as np


def constraint_function1(x_s_i):
    x = x_s_i[:4]
    i = x_s_i[12:]
    return 10 * x[0] - 400 - i[0]


def constraint_function2(x_s_i):
    x = x_s_i[:4]
    i = x_s_i[12:]
    return i[0] + 10 * x[1] - 600 - i[1]


def constraint_function3(x_s_i):
    x = x_s_i[:4]
    i = x_s_i[12:]
    return i[1] + 10 * x[2] - 400 - i[2]


def constraint_function4(x_s_i):
    x = x_s_i[:4]
    i = x_s_i[12:]
    return i[2] + 10 * x[3] - 500


def constraint_function5(x_s_i):
    x = x_s_i[:4]
    sp = x_s_i[4:8]
    sn = x_s_i[8:12]
    return x[0] - sn[0] + sp[0]


def constraint_function6(x_s_i):
    x = x_s_i[:4]
    sp = x_s_i[4:8]
    sn = x_s_i[8:12]
    return x[1] - x[0] - sn[1] + sp[1]


def constraint_function7(x_s_i):
    x = x_s_i[:4]
    sp = x_s_i[4:8]
    sn = x_s_i[8:12]
    return x[2] - x[1] - sn[2] + sp[2]


def constraint_function8(x_s_i):
    x = x_s_i[:4]
    sp = x_s_i[4:8]
    sn = x_s_i[8:12]
    return x[3] - x[2] - sn[3] + sp[3]


def constraint_function9(x_s_i):
    return np.min(x_s_i)


constraints = [constraint_function1, constraint_function2, constraint_function3, constraint_function4,
               constraint_function5, constraint_function6, constraint_function7, constraint_function8,
               constraint_function9]

types = ["eq", "eq", "eq", "eq", "eq", "eq", "eq", "eq", "ineq"]
