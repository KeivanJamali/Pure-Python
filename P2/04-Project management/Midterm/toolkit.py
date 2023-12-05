import matplotlib.pyplot as plt
import numpy as np


def u(w, s=2):
    return 100 * w ** s


def u2(W):
    return np.log10(W)


def plotting(name: str, u, s=2) -> None:
    plt.scatter(np.arange(0, 1000, 0.1), [u(i, s) for i in np.arange(0, 1000, 0.1)])
    plt.xlabel("W")
    plt.ylabel("u(W)")
    plt.title("u(W) function")
    plt.savefig(f"{name}.svg", format="svg")
    plt.show()


def expected_value(gain: list, probability: list) -> float:
    return sum([gain[i] * probability[i] for i in range(len(gain))])


def expected_utility(gain: list, probability: list, wealth: int) -> float:
    return sum([u2(gain[i] + wealth) * probability[i] for i in range(len(gain))])
