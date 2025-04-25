from modular.number_generator import Exponential_Generator, Uniform_Generator
from modular.Engine import Storage_Simulator

demand_intervals_seed = 1985072130
delay_seed = 748932582
demand_seed = 1631331038
mean = 5

demand_intervals = Uniform_Generator(seed=demand_intervals_seed)
demand = Exponential_Generator(seed=demand_seed, mean=mean)
delay = Uniform_Generator(seed=delay_seed)

def main(day_limit:int, 
         storage_initial_level:float, 
         storage_capacity_S:float, 
         storage_request_limit_s:str,
         plot_it:bool=False):
    demand_intervals = Uniform_Generator(seed=demand_intervals_seed)
    demand = Exponential_Generator(seed=demand_seed, mean=mean)
    delay = Uniform_Generator(seed=delay_seed)

    model = Storage_Simulator(demand_generator=demand,
                              demand_interval_generator=demand_intervals,
                              delay_generator=delay,
                              fixed_cost=15,
                              variable_cost=2,
                              pos_cost=5.2,
                              neg_cost=520,
                              initial_level=storage_initial_level)
    
    # [S, s]
    policies = [[storage_capacity_S, storage_request_limit_s]]
    model.fit(time_limit=day_limit, policies=policies)

    if plot_it:        
        model.plot_it()

    return model
    



