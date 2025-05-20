import numpy as np

class General_Generator:
    def __init__(self, distribution, seed:int=None):
        self.distribution = distribution
        self.seed = seed
        self.rng = np.random.default_rng(seed=seed)

    def __call__(self, *args, **kwds):
        return self.distribution.rvs(random_state=self.rng)

class Exponential_Generator:
    def __init__(self, seed:int, mean:float) -> None:
        self.mean = mean
        self.seed = seed
        self.rng = np.random.default_rng(seed=seed)

    def __call__(self):
        return self.rng.exponential(self.mean)

class Deterministic_Generator:
    def __init__(self, mean):
        self.mean = mean

    def __call__(self):
        return self.mean

