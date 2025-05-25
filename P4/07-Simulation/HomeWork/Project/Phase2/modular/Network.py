import simpy
from modular.Individual_Engine import Queue

class Network:
    def __init__(self,
                 arrival_gen,
                 sim_time_limit:int=float("inf"), 
                 sim_customer_limit:int=float("inf")):
        self.env = simpy.Environment()
        self.sim_time_limit = sim_time_limit
        self.sim_customer_limit = sim_customer_limit
        self.arrival_gen = arrival_gen
        self.service_time_gen = None
        self.stations = {}

    def add_station(self, name, capacity, in_people, service_time_gen):
        if in_people == "start":
            self.stations[name] = Queue(env=self.env,
                                        arrival_gen=self.arrival_gen,
                                        service_time_gen=service_time_gen,
                                        capacity=capacity)
        else:
            if not in_people in self.stations.keys():
                raise "[ERROR] In people should be 'start' or one of the current stations."
            else:
                self.stations[name] = Queue(env=self.env,
                                            arrival_gen=what,
                                            service_time_gen=service_time_gen,
                                            capacity=capacity)

    def run(self, policy:str, report:bool=True, detailed:bool=False):
        """Starts the simulation.
        """
        self.env.process(self._arrival_process(detailed=detailed))
        self.env.process(self._dispatcher_process(policy_function=policy, detailed=detailed))

        while True:
            self.env.step()
            if self.env.now >= self.sim_time_limit:
                print("[INFO] Time limit reached. The simulation finished successfuly.")
                self.limit_type = "T"
                break
            if self.stats["completed"] >= self.sim_customer_limit:
                print("[INFO] Customer limit reached. The simulation finished successfuly.")
                self.limit_type = "C"
                break
        self.finalize_remaining_customers()
        self.report(print_=report)