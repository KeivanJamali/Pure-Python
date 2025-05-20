import simpy

class Customer:
    def __init__(self, 
                 env:simpy.Environment, 
                 name:int, 
                 server:simpy.Resource, 
                 arrival_time:float, 
                 service_time:float, 
                 stats:dict,
                 callbacks:dict):
        """Here we have the Customer object that will process.

        Args:
            env (simpy.Environment): We pass the environment we are working in.
            name (int): The id of this customer which is a number.
            server (simpy.Resource): We pass the resource or server.
            service_time (float): We pass the calculated service time here.
            stats (dict): All the parameters we want to monitor.
        """

        self.env = env
        self.name = name
        self.server = server
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.stats = stats
        self.callbacks = callbacks
        self.action = env.process(self.process())

    def process(self):
        """The behaviour of a customer who shoud go to the server.
        """
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
