from math import log
import numpy as np


class Exponential_Generator:
    """Exponential Generator.
    """

    def __init__(self, seed: int, mean: float) -> None:
        """
        Args:
            seed (int): The initial number to start.
            mean (float): Mean of the exponential distribution.
        """
        self.mean = mean
        self.seed = seed
        self.temp = self.seed
        self.first = False

    def next_number(self) -> float:
        """Generate a number.

        Returns:
            float: Generated number.
        """
        if self.first:
            self.first = False
            u = self.temp/2147483648
            return -self.mean * log(u)
        else:
            self.temp = (16807 * self.temp) % 2147483648
            u = self.temp/2147483648
            return -self.mean * log(u)

    def reset(self):
        self.temp = self.seed
        self.first = False


class Uniform_Generator:
    """Uniform Generator.
    """

    def __init__(self, seed: int) -> None:
        """
        Args:
            seed (int): The initial number to start.
        """
        self.seed = seed
        self.temp = seed
        self.first = False

    def next_number(self) -> float:
        """Generate a number.

        Returns:
            float: Generated number.
        """
        if self.first:
            self.first = False
            u = self.temp/2147483648
            return u
        else:
            self.temp = (16807 * self.temp) % 2147483648
            u = self.temp/2147483648
            return u

    def reset(self):
        self.temp = self.seed
        self.first = False


class Deterministic_Generator:
    def __init__(self, mean):
        self.mean = mean

    def next_number(self):
        return self.mean
