import numpy as np
import matplotlib.pyplot as plt
def f2(x):
    m = (np.log10(alpha_a * PGA) - np.log10(PGA)) / (np.log10(0.125) - np.log10(0.033))
    y = m * (np.log10(x) - np.log10(0.033)) + np.log10(PGA)
    return 10 ** y
def f4(x):
    return ((2 * np.pi) / x) * ((PGV * alpha_v) / 386)
def f5(x):
    return ((2 * np.pi) / x) ** 2 * (PGD * alpha_d / 386)
def f6(x):
    m = (np.log10((((2 * np.pi) / 33) ** 2) * PGD / 386) - np.log10(
        (((2 * np.pi) / 10) ** 2) * PGD * alpha_d / 386)) / (np.log10(33) - np.log10(10))
    y = m * (np.log10(x) - np.log10(10)) + np.log10((((2 * np.pi) / 10) ** 2) * PGD * alpha_d / 386)
    return 10 ** y
def f7(x):
    return (((2 * np.pi) / x) ** 2) * (PGD / 386)
PGA = 0.5606
alpha_a = 2.71
PGV = 26.93
alpha_v = 2.3
PGD = 20.09
alpha_d = 2.01
x1 = np.arange(0, 0.033, 0.001)
y1 = [PGA for _ in range(len(x1))]
x2 = np.arange(0.033, 0.125, 0.001)
y2 = f2(x2)
x3 = np.arange(0.125, 0.665, 0.001)
y3 = [PGA * alpha_a for _ in range(len(x3))]
x4 = np.arange(0.665, 4.08, 0.001)
y4 = f4(x4)
x5 = np.arange(4.08, 10, 0.001)
y5 = f5(x5)
x6 = np.arange(10, 33, 0.001)
y6 = f6(x6)
x7 = np.arange(33, 35, 0.001)
y7 = f7(x7)
plt.plot(x1, y1, label="1")
plt.plot(x2, y2, label="2")
plt.plot(x3, y3, label="3")
plt.plot(x4, y4, label="4")
plt.plot(x5, y5, label="5")
plt.plot(x6, y6, label="6")
plt.plot(x7, y7, label="7")
plt.legend()
plt.xlabel("Period(sec)")
plt.ylabel("Pseudo-Acceleration(g)")
plt.loglog(x1, y1, label="1")
plt.loglog(x2, y2, label="2")
plt.loglog(x3, y3, label="3")
plt.loglog(x4, y4, label="4")
plt.loglog(x5, y5, label="5")
plt.loglog(x6, y6, label="6")
plt.loglog(x7, y7, label="7")
plt.legend()
plt.xlabel("Log(Period) (sec)")
plt.ylabel("Log(Pseudo-Acceleration) (g)")
plt.savefig("q5-3.svg")