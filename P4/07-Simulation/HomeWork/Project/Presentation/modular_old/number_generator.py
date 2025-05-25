from math import log

class Exponential_Generator:
    """Exponential Generator.
    """
    def __init__(self, seed:int, mean:float) -> None:
        """
        Args:
            seed (int): The initial number to start.
            mean (float): Mean of the exponential distribution.
        """
        self.mean = mean
        self.seed = seed
        self.first = True

    def next_number(self) -> float:
        """Generate a number.

        Returns:
            float: Generated number.
        """
        if self.first:
            self.first = False
            u = self.seed/2147483648
            return -self.mean * log(u)
        else:
            self.seed = (16807 * self.seed)%2147483648
            u = self.seed/2147483648
            return -self.mean * log(u)

class Deterministic_Generator:
    def __init__(self, mean):
        self.mean = mean

    def next_number(self):
        return self.mean

