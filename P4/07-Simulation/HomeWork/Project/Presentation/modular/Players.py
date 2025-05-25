import simpy

class Customer:
    def __init__(self, 
                 id:int,
                 env:simpy.Environment, 
                 server:simpy.Resource, 
                 arrival_time:float, 
                 service_time:float, 
                 stats:dict,
                 _callbacks:dict):
        """Here we have the Customer object that will process.

        Args:
            env (simpy.Environment): We pass the environment we are working in.
            id (int): The id of this customer which is a number.
            server (simpy.Resource): We pass the resource or server.
            arrival_time (float): We pass the calculated arrival time here.
            service_time (float): We pass the calculated service time here.
            stats (dict): All the parameters we want to monitor.
            _callback (dict, private variable): Do not change this variable, it will call Engine whenever is needed. Warning!!!
        """

        self.env = env
        self.id = id
        self.server = server
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.stats = stats
        self._callbacks = _callbacks
        self.action = None

    def active(self):
        """Activate customers. Customer starts to do it's job."""
        self.action = self.env.process(self.process())

    def process(self):
        """The behaviour of a customer who shoud go to the server."""
        with self.server.request() as request:
            yield request

            wait_time_in_queue = self.env.now - self.arrival_time

            yield self.env.timeout(self.service_time)

            wait_time_in_system = wait_time_in_queue + self.service_time
            self.stats["Wait_time_in_system"].append(wait_time_in_system)
            self.stats["Wait_time_in_queue"].append(wait_time_in_queue)
            self.stats["Waits_more"] += 1 if wait_time_in_system > 4.5 else 0
            self.stats["Integral_of_curve"] += wait_time_in_system
            self.stats["completed"] += 1

            if not self._callbacks["dispatcher_event"].triggered:
                self._callbacks["dispatcher_event"].succeed(self.id)
            self._callbacks["dispatcher_event"] = self.env.event()
        
