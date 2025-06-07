import pandas as pd
from modular.Individual_Engine import Queue
from modular.Number_Generator import Exponential_Generator, Deterministic_Generator


class Queue_Program:
    """By using Queue, we can run multiple replication from a system and gather the results in a dataframe.
    """
    def __init__(self,
                 seed_pairs:list,
                 mean_pair:list,
                 generator_pair:list,
                 policy,
                 sim_time_limit:float=float("inf"), 
                 sim_customer_limit:int=float("inf"),
                 capacity:int=1):
        """Initializing.
        Args:
            seed_pairs (list): Here there should be the pair of seeds for (arrival gen, service_time gen).
            mean_pair (list): (arrival_mean time, service_time mean time) as a list.
            generator_pair (list): ('Expo', 'Expo') list of two str. For now we support only 'Expo':exponential and 'Deter':Deterministic.
            policy (Python Function): This function is a python function where input=wait customers as a list of (customer_id, customer_data). 
                                      The output should be a int number which shows the customer_id of the chosen customer.
            sim_time_limit (float, optional): If you want can say a limit for the time of simulation. Defaults to float("inf").
            sim_customer_limit (int, optional): If you want you can set the max served customer. Defaults to float("inf").
            capacity (int, optional): The capacity of server. Defaults to 1.
        """
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
        """Start simulating..."""
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
        """Here you can change the generator types as you like. Here we put two Expo and Deter generators.
           These functions are giving a random number when you call their object. For example:
           gen = Exponential_Generator(42, 5)
           print('You should see a float number here:', gen())

        Raises:
            ValueError: If you send some str other than Expo and Deter this error will raise.
        """
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
