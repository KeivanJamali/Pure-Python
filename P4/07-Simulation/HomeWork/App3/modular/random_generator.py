import random

class Expo_Gen:
    def __init__(self, mean:float, seed:int=None):
        self.rnd = random.Random(seed)
        self.mean = mean

    def generate(self):
        return self.rnd.expovariate(1/self.mean)

    def __call__(self):
        return self.generate()
    

class Deterministic_Gen:
    def __init__(self, mean:float, seed:int=None):
        self.rnd = random.Random(seed)
        self.mean = mean

    def generate(self):
        return self.mean

    def __call__(self):
        return self.generate()