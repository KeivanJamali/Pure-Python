import pandas as pd
from modular.Individual_Engine import Queue
from modular.Number_Generator import Exponential_Generator, Deterministic_Generator


class Queue_Program:
    def __init__(self,
                 seed_pairs:list,
                 mean_pair:list,
                 generator_pair:list,
                 policy,
                 sim_time_limit:float=float("inf"), 
                 sim_customer_limit:int=float("inf"),
                 capacity:int=1):
        self.seed_pairs = seed_pairs
        self.capacity = capacity
        self.mean_pair = mean_pair
        self.generator_pair = generator_pair
        self._set_generators()
        self.sim_time_limit = sim_time_limit
        self.sim_customer_limit = sim_customer_limit
        self.policy = policy
        self.result = None

    def run(self):
        result = [] 
        for i in range(len(self.seed_pairs)):
            model = Queue(arrival_gen=self.arrival_gens[i],
                          service_time_gen=self.service_time_gens[i],
                          sim_time_limit=self.sim_time_limit,
                          sim_customer_limit=self.sim_customer_limit,
                          capacity=self.capacity)
            model.run(policy=self.policy, detailed=False, report=False)
            model.report_data["seed_pair"] = self.seed_pairs[i]
            result.append(model.report_data)
        self.result = pd.DataFrame(result)

    def _set_generators(self):
        if self.generator_pair[0].lower() == "expo":
            self.arrival_gens = [Exponential_Generator(seed=s[0], mean=self.mean_pair[0]) for s in self.seed_pairs]
        elif self.generator_pair[0].lower() == "deter":
            self.arrival_gens = [Deterministic_Generator(mean=self.mean_pair[0]) for s in self.seed_pairs]
        else:
            raise ValueError("We only support Expo and Deter for now.")

        if self.generator_pair[1].lower() == "expo":
            self.service_time_gens = [Exponential_Generator(seed=s[1], mean=self.mean_pair[1]) for s in self.seed_pairs]
        elif self.generator_pair[1].lower() == "deter":
            self.service_time_gens = [Deterministic_Generator(mean=self.mean_pair[1]) for s in self.seed_pairs]
        else:
            raise ValueError("We only support Expo and Deter for now.")
