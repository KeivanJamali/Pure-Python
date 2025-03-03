from modular import Engine
from modular.number_generator import Exponential_Generator
import time

# Custom input
class Generator:
    def __init__(self, data):
        self.data = data
        self.counter = -1

    def next_number(self):
        self.counter += 1
        return self.data[self.counter]
data1 = [3, 3, 2, 4, 6, 2, 4, 8, 4, 5, 5]
data2 = [6, 4, 2, 2, 4, 3, 4, 6, 4, 3, 6]

data1 = [55, 32, 24, 40, 12, 29]
data2 = [43, 36, 34, 16, 25, 19]

gen1 = Generator(data1)
gen2 = Generator(data2)

interval_generator = Exponential_Generator(seed=2062615503, mean=5)
service_time_generator = Exponential_Generator(seed=1383670351, mean=4)


