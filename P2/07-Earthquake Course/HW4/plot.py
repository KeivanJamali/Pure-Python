from matplotlib import pyplot as plt
import numpy as np

a1 = 0.8
a2 = 0.68


def f1(x):
    u = 1 - np.cos(2 * np.pi * x)
    return u


def f2(x, tt):
    u = (1 - np.cos(2 * np.pi * tt)) * (np.cos(2 * np.pi * (x - tt)))
    u = u + np.sin(2 * np.pi * tt) * np.sin(2 * np.pi * (x - tt))
    return u


def plot(f, range_f: list, g, range_g: list, tt, number):
    x1 = np.arange(range_f[0], range_f[1], 0.01)
    y1 = f(x1)
    x2 = np.arange(range_g[0], range_g[1], 0.01)
    y2 = g(x2, tt)
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.savefig(f"q2-{number}.svg")
    plt.show()


# tt = 0.15 + 0.1 * a1
# tt = 0.5 + 0.3 * a2
tt = 1.5 + a1
plot(f=f1, range_f=[0, tt], g=f2, range_g=[tt, 6], tt=tt, number=3)
print(tt)
