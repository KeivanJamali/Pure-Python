import simpy
from modular.Players import Customer

class One_Server_Queue:
    def __init__(self, 
                 arrival_gen:float,
                 service_time_gen:float,
                 sim_time_limit:int=float("inf"), 
                 sim_customer_limit:int=float("inf"),
                 capacity:int=1):
        """Make a MM1 Queue with FCFS policy.

        Args:
            arrival_gen (float): Generator that produce inter-arrival time.
            service_time_gen (float): Generator that produce service time.
            sim_time_limit (int, optional): If you want can say a limit for the time of simulation. Defaults to float("inf").
            sim_customer_limit (int, optional): If you want you can set the max served customer. Defaults to float("inf").
            capacity (int, optional): The capacity of server.
        """
        self.arrival_gen = arrival_gen
        self.service_time_gen = service_time_gen
        self.sim_time_limit = sim_time_limit
        self.sim_customer_limit = sim_customer_limit
        self.env = simpy.Environment()
        self.server = simpy.Resource(self.env, capacity=capacity)
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
        self.report_data = {}

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

    def run(self, policy:str, report:bool=True):
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
                print("[INFO] Time limit reached. The simulation finished successfuly.")
                self.limit_type = "T"
                break
            if self.stats["completed"] >= self.sim_customer_limit:
                print("[INFO] Customer limit reached. The simulation finished successfuly.")
                self.limit_type = "C"
                break
        self.finalize_remaining_customers()
        self.report(print_=report)

    def report(self, print_):
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
        if print_:
            print(f"\n--- Simulation Report ---")
            print(f"Total customers arrived: {self.customer_count}")
            print(f"Average wait time in queue: {avg_waiting_time_in_queue:.2f}")
            print(f"Average wait time in system: {avg_waiting_time_in_system:.2f}")
            # print(f"Average number in queue: {avg_system_length - utilization:.2}")
            print(f"Average number in system: {avg_system_length:.2}")
            # print(f"Server utilization: {100 * utilization:.2f}%")
            # print(
                # f"Percent of customers who waited > 4.5 min: {percent_over_45:.2f}%")
            print(f"Simulation ended at time: {total_time:.2f} with {completed_customers} customer served.")

        self.report_data = {"total_time": total_time,
                            "arrived":self.customer_count,
                            "served":completed_customers,
                            "wait_time_queue":avg_waiting_time_in_queue,
                            "wait_time_system":avg_waiting_time_in_system,
                            "number_system":avg_system_length}


