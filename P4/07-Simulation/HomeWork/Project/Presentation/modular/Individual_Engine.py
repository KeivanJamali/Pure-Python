import simpy
from modular.Players import Customer

class Queue:
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
        self.capacity = capacity
        self.stats = {"Wait_time_in_queue": [],
                      "Wait_time_in_system": [],
                      "Waits_more": 0,
                      "Integral_of_curve": 0,
                      "completed":0}
        self.customer_id = 0
        self.callbacks = {"dispatcher_event": self.env.event(),
                          "customer_arrived_event": self.env.event()}
        self.customer_in_system = {}
        self.customers_in_queue = []
        self.limit_type = None
        self.report_data = {}

    def _arrival_process(self, detailed=False):
        """Send customers in queue. This function is a generator used for env.
        """
        while True:
            interarrival = self.arrival_gen()
            service_time = self.service_time_gen()
            yield self.env.timeout(interarrival)

            customer = {
                "id": self.customer_id,
                "env": self.env,
                "server": self.server,
                "arrival_time": self.env.now,
                "service_time": service_time,
                "stats": self.stats,
                "callbacks": self.callbacks,
            }

            self.customer_in_system[self.customer_id] = Customer(**customer)
            self.customers_in_queue.append((self.customer_id, customer))

            if detailed:
                print(f"[ARRIVE] Customer {self.customer_id} generated. Added to system and queue.")

            # Tell everyone that a customer arrived.
            if not self.callbacks["customer_arrived_event"].triggered:
                self.callbacks["customer_arrived_event"].succeed(self.customer_id)

            # Reset the event for next customer.
            self.customer_id += 1
            self.callbacks["customer_arrived_event"] = self.env.event()

    def _dispatcher_process(self, policy_function, detailed:bool):
        """Continuously checks and dispatches the customer according to the policy function."""
        while True:
            if len(self.customers_in_queue) == 0 and len(self.server.users) == 0:
                customer_id = yield self.callbacks["customer_arrived_event"]
                self.customer_in_system[customer_id].active()
                self.customers_in_queue.pop(0)
                if detailed:
                    print(f"[ZERO] As no one where in queue or server, we activate customer {customer_id} and remove it from queue.")

            result_event = yield self.callbacks["customer_arrived_event"] | self.callbacks["dispatcher_event"]
            if len(self.server.users) < self.server.capacity and len(self.customers_in_queue) > 0:
                if self.callbacks["dispatcher_event"] in result_event:
                    customer_id = yield self.callbacks["dispatcher_event"]
                    del self.customer_in_system[customer_id]
                    if detailed:
                        print(f"[QUITE] Customer {customer_id}")
                customer_id = policy_function(customers_in_waitlist=self.customers_in_queue)
                self.customer_in_system[customer_id].active()
                if detailed:
                    print(f"[DISPATCH] Customer {customer_id} goes to server according to the policy.")

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
    
    def finalize_remaining_customers(self):
        """It will take care of the last people who are still in the queue and not finished yet, but we need their presece
        to find the total integral of the curve.
        """
        for customer_id, customer in self.customers_in_queue:
            wait_time_so_far = self.env.now - customer["arrival_time"]
            if wait_time_so_far > 4.5:
                self.stats["Waits_more"] += 1
            self.stats["Integral_of_curve"] += wait_time_so_far

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
        utilization = (sum(self.stats["Wait_time_in_system"]) - sum(self.stats["Wait_time_in_queue"])) / total_time
        if print_:
            print(f"\n--- Simulation Report ---")
            print(f"Total customers arrived: {self.customer_id+1}")
            print(f"Average wait time in queue: {avg_waiting_time_in_queue:.2f}")
            print(f"Average wait time in system: {avg_waiting_time_in_system:.2f}")
            # print(f"Average number in queue: {avg_system_length - utilization:.2}")
            print(f"Average number in system: {avg_system_length:.2}")
            print(f"Server utilization: {(100 / self.capacity) * utilization:.2f}%")
            # print(
                # f"Percent of customers who waited > 4.5 min: {percent_over_45:.2f}%")
            print(f"Simulation ended at time: {total_time:.2f} with {completed_customers} customer served.")

        self.report_data = {"total_time": total_time,
                            "arrived":self.customer_id+1,
                            "served":completed_customers,
                            "wait_time_queue":avg_waiting_time_in_queue,
                            "wait_time_system":avg_waiting_time_in_system,
                            "number_system":avg_system_length,
                            "Utilization":utilization*100/self.capacity}


