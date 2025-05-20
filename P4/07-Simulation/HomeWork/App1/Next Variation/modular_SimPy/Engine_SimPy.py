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



class All_Type_Queue:
    def __init__(self, 
                 arrival_gen:float,
                 service_time_gen:float,
                 sim_time_limit:int=float("inf"), 
                 sim_customer_limit:int=float("inf")):
        """Make a MM1 Queue with FCFS policy.

        Args:
            mean_arrival (float): _description_
            mean_service_time (float): _description_
            sim_time_limit (int, optional): _description_. Defaults to float("inf").
            sim_customer_limit (int, optional): _description_. Defaults to float("inf").
            random_seed0 (int, optional): _description_. Defaults to 42.
            random_seed1 (int, optional): _description_. Defaults to 42.
        """
        
        self.arrival_gen = arrival_gen
        self.service_time_gen = service_time_gen
        self.sim_time_limit = sim_time_limit
        self.sim_customer_limit = sim_customer_limit
        self.env = simpy.Environment()
        self.server = simpy.Resource(self.env, capacity=1)
        self.stats = {"Wait_time_in_queue": [],
                      "Wait_time_in_system": [],
                      "Waits_more": 0,
                      "Integral_of_curve": 0,
                      "Busy_server_time": 0,
                      "completed":0}
        self.callbacks = {"dispatcher_event": self.env.event(),
                          "customer_arrived_event": self.env.event()}
        self.customer_count = 0
        self.customer_in_system = []
        self.customer_in_waitlist = []
        self.limit_type = None

    def fcfs_arrival_process(self):
        """Send customers in queue with FCFS policy. This function is a generator used for env.
        """
        while True:
            interarrival = self.arrival_gen()
            servicetime = self.service_time_gen()
            yield self.env.timeout(interarrival)

            self.customer_count += 1
            name = f"Customer {self.customer_count}"
            self.customer_in_system.append(Customer(env=self.env,
                                                   name=name,
                                                   server=self.server,
                                                   arrival_time=self.env.now,
                                                   service_time=servicetime,
                                                   stats=self.stats,
                                                   callbacks=self.callbacks))
            
    def spt_arrival_process(self):
        """Generates arriving customers and adds them to the waiting list."""
        while True:
            interarrival = self.arrival_gen()
            service_time = self.service_time_gen()
            yield self.env.timeout(interarrival)

            self.customer_count += 1
            name = f"Customer {self.customer_count}"

            customer = {
                "env": self.env,
                "name": name,
                "server": self.server,
                "arrival_time": self.env.now,
                "service_time": service_time,
                "stats": self.stats,
                "callbacks": self.callbacks,
            }

            self.customer_count += 1
            self.customer_in_waitlist.append(customer)

            # Trigger the event
            if not self.callbacks["customer_arrived_event"].triggered:
                self.callbacks["customer_arrived_event"].succeed()

            # Reset the event for next use
            self.callbacks["customer_arrived_event"] = self.env.event()

    def spt_dispatcher_process(self):
        """Continuously checks and dispatches the shortest-service-time customer."""
        while True:
            yield self.callbacks["customer_arrived_event"] | self.callbacks["dispatcher_event"]

            if not self.callbacks["customer_arrived_event"].triggered:
                self.callbacks["customer_arrived_event"] = self.env.event()
            if not self.callbacks["dispatcher_event"].triggered:
                self.callbacks["dispatcher_event"] = self.env.event()

            if len(self.customer_in_waitlist) > 0 and len(self.server.users) == 0:
                self.customer_in_waitlist.sort(key=lambda c: c["service_time"])
                chosen = self.customer_in_waitlist.pop(0)
                self.customer_in_system.append(Customer(**chosen))
            
    def finalize_remaining_customers(self):
        """It will take care of the last people who are still in the queue and not finished yet, but we need their presece
        to find the total integral of the curve.
        """
        for customer in self.customer_in_system:
            if not customer.action.triggered:  # Still running = not finished process
                wait_time_so_far = self.env.now - customer.arrival_time
                self.stats["Integral_of_curve"] += wait_time_so_far

    def run(self, policy:str):
        """Starts the simulation.
        """
        if policy.lower() == "fcfs":
            self.env.process(self.fcfs_arrival_process())
        elif policy.lower() == "spt":
            self.env.process(self.spt_arrival_process())
            self.env.process(self.spt_dispatcher_process())
        else:
            raise ValueError("[ERROR] We only support two policy: SPF - FCFS.")

        while True:
            self.env.step()
            if self.env.now >= self.sim_time_limit:
                print("[INFO] Time limit reached.")
                self.limit_type = "T"
                break
            if self.stats["completed"] >= self.sim_customer_limit:
                print("[INFO] Customer limit reached.")
                self.limit_type = "C"
                break
        self.finalize_remaining_customers()
        self.report()

    def report(self):
        """Give a report.
        """
        if self.limit_type == "C":
            total_time = self.env.now
        elif self.limit_type == "T":
            total_time = self.sim_time_limit
        completed_customers = len(self.stats["Wait_time_in_queue"])
        avg_waiting_time_in_queue = sum(self.stats["Wait_time_in_queue"]) / completed_customers
        avg_waiting_time_in_system = sum(self.stats["Wait_time_in_system"]) / completed_customers
        percent_over_45 = 100 * self.stats["Waits_more"] / completed_customers
        avg_system_length = self.stats["Integral_of_curve"] / total_time
        utilization = self.stats["Busy_server_time"] / total_time

        print(f"\n--- Simulation Report ---")
        print(f"Total customers served: {self.customer_count}")
        print(f"Average wait time in queue: {avg_waiting_time_in_queue:.2f}")
        print(f"Average wait time in system: {avg_waiting_time_in_system:.2f}")
        # print(f"Average number in queue: {avg_system_length - utilization:.2}")
        print(f"Average number in system: {avg_system_length:.2}")
        # print(f"Server utilization: {100 * utilization:.2f}%")
        # print(
            # f"Percent of customers who waited > 4.5 min: {percent_over_45:.2f}%")
        print(f"Simulation ended at time: {total_time:.2f} with {completed_customers} customer served.")


