import numpy as np
import matplotlib.pyplot as plt

a = 0.8
zeta1 = 0.000001
zeta2 = 0.106


def f1(x, z):
    print((np.sqrt(1 - z ** 2)) / z)
    y = x * np.exp((-z / (np.sqrt(1 - z ** 2))) * np.tan((np.sqrt(1 - z ** 2)) / z) ** (-1))
    return y


def f2(x, z):
    y = ((2 * np.pi) / (x)) * np.exp((-z / (np.sqrt(1 - z ** 2))) * np.tan((np.sqrt(1 - z ** 2)) / z) ** (-1))
    return y


def f3(x, z):
    y = np.exp((-z / (np.sqrt(1 - z ** 2))) * np.tan((np.sqrt(1 - z ** 2)) / z) ** (-1))
    return [y for _ in range(len(x))]


def plot(f, zeta1, zeta2, number: int):
    x1 = np.arange(0.1, 30, 0.1)
    x2 = np.arange(0.0265, 30, 0.1)
    y1 = f(x1, zeta1)
    y2 = f(x1, zeta2)
    plt.plot(x1, y1, label="zeta = 0")
    plt.plot(x1, y2, label="zeta = 10.6")
    plt.legend()
    plt.xlabel("s")
    name = ["Deformation", "Pseudo-Acceleration", "Pseudo-Velocity"]
    plt.ylabel(name[number - 1])
    plt.savefig(f"q3-{number}.svg")
    plt.show()


plot(f=f3, zeta1=zeta1, zeta2=zeta2, number=3)
