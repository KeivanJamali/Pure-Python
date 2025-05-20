from modular.number_generator import Exponential_Generator, Deterministic_Generator
from modular.Engine import Queue_Simulator

mean0, mean1 = 4, 4.5
        
def main(policy:str, 
         stop_type:str, 
         stop_limit:float, 
         queue_type:str,
         print_:bool=False,
         detailed:bool=False,
         plot_it:bool=False,
         Y0:int=[2062615503],
         Y1:int=[1383670351]):
    if stop_type.lower() not in ["time", "customer"]:
        raise ValueError("Wrong type for Stop_type. Chose between ['Time' and 'Customer']")
    if queue_type.lower() not in ["mmi", "mdi"]:
        raise ValueError("Wrong type for queue_type. Chose between ['MMI' and 'MDI']")
    if policy.lower() not in ["fcfs", "spt"]:
        raise ValueError("Wrong type for Stop_type. Chose between ['FCFS' and 'SPT']")
    for i in range(len(Y0)):
        if stop_type.lower() == "time":
            if queue_type.lower() == "mmi":
                gen1 = Exponential_Generator(seed=Y0[i], mean=mean0)
                gen2 = Exponential_Generator(seed=Y1[i], mean=mean1)
                model = Queue_Simulator(interval_generator=gen1,
                                        service_time_generator=gen2,
                                        print_=print_,
                                        detailed=detailed)
                model.fit(policy=policy, last_time=stop_limit)
            elif queue_type.lower() == "mdi":
                gen1 = Exponential_Generator(seed=Y0[i], mean=mean0)
                gen2 = Deterministic_Generator(mean=mean1)
                model = Queue_Simulator(interval_generator=gen1,
                                        service_time_generator=gen2,
                                        print_=print_,
                                        detailed=detailed)
                model.fit(policy=policy, last_time=stop_limit)

        if stop_type.lower() == "customer":
            if queue_type.lower() == "mmi":
                gen1 = Exponential_Generator(seed=Y0[i], mean=mean0)
                gen2 = Exponential_Generator(seed=Y1[i], mean=mean1)
                model = Queue_Simulator(interval_generator=gen1,
                                        service_time_generator=gen2,
                                        print_=print_,
                                        detailed=detailed)
                model.fit(policy=policy, last_id=stop_limit)
            elif queue_type.lower() == "mdi":
                gen1 = Deterministic_Generator(mean=mean0)
                gen2 = Deterministic_Generator(mean=mean1)
                model = Queue_Simulator(interval_generator=gen1,
                                        service_time_generator=gen2,
                                        print_=print_,
                                        detailed=detailed)
                model.fit(policy=policy, last_id=stop_limit)        

    if plot_it:        
        model.plot_sample_path(file_name="sample.svg")

    return model
    



