import simpy
import random
from modular.Players import Customer
from modular.Number_Generator import Exponential_Generator

class Queue_Network:
    def __init__(self):
        self.env = simpy.Environment()
        self.customer_id = 0

    def set_setting(self):
        """You must rewrite this function as you like."""
        self.arrival_gens = {"station1":Exponential_Generator(seed=42, mean=5)}
        self.service_time_gens = {"station1":Exponential_Generator(seed=42, mean=4)}

    def run(self):
        pass

    def arrival_process(self, arrival_gen, service_time_gen, server):
        intervals = arrival_gen()
        service_times = service_time_gen()

        yield self.env.timeout(intervals)

        name = f"C{self.customer_id}"
        self.customer_id += 1
        customer_data = {
                        "env": self.env,
                        "name": name,
                        "server": server,
                        "arrival_time": self.env.now,
                        "stats": self.stats,
                        "callbacks": self.callbacks,
            }


    def dispatcher(self, customer):
        pass



