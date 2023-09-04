import matplotlib.pyplot as plt
import numpy as np

B = 1
L = 2
z = 1
max = []
may = []
maz = []

for i in range(B * 100):
    for j in range(L * 100):
        max.append(i)
        may.append(j)
        m2 = i / z
        n2 = j / z
        I2 = (1 / (4 * np.pi)) * (((2 * m2 * n2 * (np.sqrt((m2 ** 2) + n2 ** 2 + 1)) / (
                    m2 ** 2 + n2 ** 2 + m2 ** 2 * n2 ** 2 + 1)) * (
                                               (2 + m2 ** 2 + n2 ** 2) / (1 + n2 ** 2 + m2 ** 2))) + np.arctan(
            (2 * m2 * n2 * np.sqrt(m2 ** 2 + n2 ** 2 + 1)) / (m2 ** 2 + n2 ** 2 + 1 - m2 ** 2 * n2 ** 2)))

        m2 = (B - i) / z
        n2 = j / z
        I1 = (1 / (4 * np.pi)) * (((2 * m2 * n2 * (np.sqrt((m2 ** 2) + n2 ** 2 + 1)) / (
                    m2 ** 2 + n2 ** 2 + m2 ** 2 * n2 ** 2 + 1)) * (
                                               (2 + m2 ** 2 + n2 ** 2) / (1 + n2 ** 2 + m2 ** 2))) + np.arctan(
            (2 * m2 * n2 * np.sqrt(m2 ** 2 + n2 ** 2 + 1)) / (m2 ** 2 + n2 ** 2 + 1 - m2 ** 2 * n2 ** 2)))

        m2 = i / z
        n2 = (L - j) / z
        I4 = (1 / (4 * np.pi)) * (((2 * m2 * n2 * (np.sqrt((m2 ** 2) + n2 ** 2 + 1)) / (
                    m2 ** 2 + n2 ** 2 + m2 ** 2 * n2 ** 2 + 1)) * (
                                               (2 + m2 ** 2 + n2 ** 2) / (1 + n2 ** 2 + m2 ** 2))) + np.arctan(
            (2 * m2 * n2 * np.sqrt(m2 ** 2 + n2 ** 2 + 1)) / (m2 ** 2 + n2 ** 2 + 1 - m2 ** 2 * n2 ** 2)))

        m2 = (B - i) / z
        n2 = (L - j) / z
        I3 = (1 / (4 * np.pi)) * (((2 * m2 * n2 * (np.sqrt((m2 ** 2) + n2 ** 2 + 1)) / (
                    m2 ** 2 + n2 ** 2 + m2 ** 2 * n2 ** 2 + 1)) * (
                                               (2 + m2 ** 2 + n2 ** 2) / (1 + n2 ** 2 + m2 ** 2))) + np.arctan(
            (2 * m2 * n2 * np.sqrt(m2 ** 2 + n2 ** 2 + 1)) / (m2 ** 2 + n2 ** 2 + 1 - m2 ** 2 * n2 ** 2)))

        I = I1 + I2 + I3 + I4
        maz.append(I)

ax1 = plt.axes(projection="3d")
ax1.scatter3D(max, may, maz)
print(max)
print(may)
plt.show()
print(maz)

