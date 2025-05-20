import simpy

class Customer:
    def __init__(self, 
                 env: simpy.Environment,
                 name:int,
                 itinerary:list[str, float],
                 arrival_time:float,
                 stats:dict):
        self.env = env
        self.name = name
        self.itinerary = itinerary
        self.arrival_time = arrival_time
        self.current_index = 0
        self.completed = False
        self.visit_logs = []
        self.stats = stats

    def _has_more_visits(self):
        return self.current_index < len(self.itinerary)
    
    def get_next_visit(self):
        if not self._has_more_visits():
            self.completed = True
            return None
        
        station_name, service_time = self.itinerary[self.current_index]
        self.current_index += 1
        visit = Visit(self.env, self, station_name, service_time)
        self.visit_logs.append(visit)
        return visit


    def process(self):
        with self.server.request() as request:
            yield request  

            wait_time_in_queue = self.env.now - self.arrival_time 

            yield self.env.timeout(self.service_time)

            wait_time_in_system = self.env.now - self.arrival_time 
            self.stats["Wait_time_in_system"].append(
                wait_time_in_system)
            self.stats["Wait_time_in_queue"].append(wait_time_in_queue)
            self.stats["Busy_server_time"] += self.service_time
            self.stats["Waits_more"] += 1 if wait_time_in_system > 4.5 else 0
            self.stats["Integral_of_curve"] += wait_time_in_system
            self.stats["completed"] += 1
            if not self.callbacks["dispatcher_event"].triggered:
                self.callbacks["dispatcher_event"].succeed()
            self.callbacks["dispatcher_event"] = self.env.event()


class Visit:
    def __init__(self,
                 env:simpy.Environment,
                 customer:Customer, 
                 station_name:str, 
                 service_time:float):
        self.env = env
        self.customer = customer
        self.station_name = station_name
        self.service_time = service_time
        self.arrival_time = customer.env.now
        self.end_time = None