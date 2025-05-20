import simpy

class Customer0:
    def __init__(self, 
                 env:simpy.Environment, 
                 name:int, 
                 server1:simpy.Resource,
                 server2:simpy.Resource,
                 arrival_time:float,
                 service_time1:float,
                 service_time2:float,
                 go_to_server2:bool,
                 stats1:dict,
                 stats2:dict,
                 callbacks1:dict,
                 callbacks2:dict):
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
        self.server1 = server1
        self.server2 = server2
        self.arrival_time1 = arrival_time
        self.arrival_time2 = None
        self.service_time1 = service_time1
        self.service_time2 = service_time2
        self.stats1 = stats1
        self.stats2 = stats2
        self.callbacks1 = callbacks1
        self.callbacks2 = callbacks2
        self.action1 = self.env.process(self.process_server_1())
        self.action2 = self.env.process(self.process_server_2()) if go_to_server2 else 0

    def process_server_1(self):
        """The behaviour of a customer who shoud go to the server 1.
        """
        with self.server1.request() as request:
            yield request  

            wait_time_in_queue1 = self.env.now - self.arrival_time1

            yield self.env.timeout(self.service_time1)

            self.arrival_time2 = self.env.now
            wait_time_in_system = self.env.now - self.arrival_time1
            self.stats1["Wait_time_in_system"].append(
                wait_time_in_system)
            self.stats1["Wait_time_in_queue"].append(wait_time_in_queue1)
            self.stats1["Busy_server_time"] += self.service_time1
            self.stats1["Integral_of_curve"] += wait_time_in_system
            self.stats1["completed"] += 1
            if not self.callbacks1["dispatcher_event"].triggered:
                self.callbacks1["dispatcher_event"].succeed()
            self.callbacks1["dispatcher_event"] = self.env.event()

    def process_server_2(self):
        """The behaviour of a customer who shoud go to the server 2.
        """
        yield self.callbacks1["dispatcher_event"]

        self.arrival_time2 = self.env.now

        with self.server2.request() as request:
            yield request  

            wait_time_in_queue2 = self.env.now - self.arrival_time2

            yield self.env.timeout(self.service_time2)

            wait_time_in_system = self.env.now - self.arrival_time2
            self.stats2["Wait_time_in_system"].append(
                wait_time_in_system)
            self.stats2["Wait_time_in_queue"].append(wait_time_in_queue2)
            self.stats2["Busy_server_time"] += self.service_time2
            self.stats2["Integral_of_curve"] += wait_time_in_system
            self.stats2["completed"] += 1
            if not self.callbacks2["dispatcher_event"].triggered:
                self.callbacks2["dispatcher_event"].succeed()
            self.callbacks2["dispatcher_event"] = self.env.event()



class Customer1:
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
