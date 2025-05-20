import simpy
import random
from modular.Players import Customer0, Customer1

class Queue_Network:
    def __init__(self, 
                 arrival_gen1:float,
                 arrival_gen2:float,
                 service_time_gen1:float,
                 service_time_gen2:float,
                 sim_time_limit:int=float("inf"), 
                 sim_customer_limit:int=float("inf"),
                 capacity1:int=1,
                 capacity2:int=1):
        """Make a MM1 Queue with FCFS policy.

        Args:
            arrival_gen (float): Generator that produce inter-arrival time.
            service_time_gen (float): Generator that produce service time.
            sim_time_limit (int, optional): If you want can say a limit for the time of simulation. Defaults to float("inf").
            sim_customer_limit (int, optional): If you want you can set the max served customer. Defaults to float("inf").
            capacity (int, optional): The capacity of server.
        """
        self.arrival_gen1 = arrival_gen1
        self.arrival_gen2 = arrival_gen2
        self.service_time_gen1 = service_time_gen1
        self.service_time_gen2 = service_time_gen2
        self.sim_time_limit = sim_time_limit
        self.sim_customer_limit = sim_customer_limit
        self.env = simpy.Environment()
        self.server1 = simpy.Resource(self.env, capacity=capacity1)
        self.server2 = simpy.Resource(self.env, capacity=capacity2)
        self.stats1 = {"Wait_time_in_queue": [],
                      "Wait_time_in_system": [],
                      "Waits_more": 0,
                      "Integral_of_curve": 0,
                      "Busy_server_time": 0,
                      "completed":0}
        self.stats2 = {"Wait_time_in_queue": [],
                      "Wait_time_in_system": [],
                      "Waits_more": 0,
                      "Integral_of_curve": 0,
                      "Busy_server_time": 0,
                      "completed":0}
        self.callbacks1 = {"dispatcher_event": self.env.event(),
                          "customer_arrived_event": self.env.event()}
        self.callbacks2 = {"dispatcher_event": self.env.event(),
                          "customer_arrived_event": self.env.event()}
        self.customer_count = 0
        self.customer_in_system = []
        self.limit_type = None
        self.report_data1 = {}
        self.report_data2 = {}

    def fcfs_arrival_process1(self):
        """Send customers in queue with FCFS policy. This function is a generator used for env.
        """
        while True:
            interarrival = self.arrival_gen1()
            servicetime1 = self.service_time_gen1()
            servicetime2 = self.service_time_gen2()
            go_to_next = random.random()>0.5
            yield self.env.timeout(interarrival)

            self.customer_count += 1
            name = f"Customer {self.customer_count}"
            self.customer_in_system.append(Customer0(env=self.env,
                                                   name=name,
                                                   server1=self.server1,
                                                   server2=self.server2,
                                                   arrival_time=self.env.now,
                                                   service_time1=servicetime1,
                                                   service_time2=servicetime2,
                                                   go_to_server2=go_to_next,
                                                   stats1=self.stats1,
                                                   stats2=self.stats2,
                                                   callbacks1=self.callbacks1,
                                                   callbacks2=self.callbacks2))
            

    def fcfs_arrival_process2(self):
        """Send customers in queue with FCFS policy. This function is a generator used for env.
        """
        while True:
            interarrival = self.arrival_gen2()
            servicetime1 = self.service_time_gen1()
            servicetime2 = self.service_time_gen2()
            go_to_next = random.random()>0.5
            yield self.env.timeout(interarrival)

            self.customer_count += 1
            name = f"Customer {self.customer_count}"
            self.customer_in_system.append(Customer1(env=self.env,
                                                   name=name,
                                                   server=self.server2,
                                                   arrival_time=self.env.now,
                                                   service_time=servicetime2,
                                                   stats=self.stats2,
                                                   callbacks=self.callbacks2))            
            
    # def finalize_remaining_customers(self):
    #     """It will take care of the last people who are still in the queue and not finished yet, but we need their presece
    #     to find the total integral of the curve.
    #     """
    #     for customer in self.customer_in_system:
    #         if not customer.action.triggered:  # Still running = not finished process
    #             wait_time_so_far = self.env.now - customer.arrival_time
    #             self.stats["Integral_of_curve"] += wait_time_so_far

    def run(self, policy:str, report:bool=True):
        """Starts the simulation.
        """
        if policy.lower() == "fcfs":
            self.env.process(self.fcfs_arrival_process1())
            self.env.process(self.fcfs_arrival_process2())

        while True:
            self.env.step()
            if self.env.now >= self.sim_time_limit:
                print("[INFO] Time limit reached. The simulation finished successfuly.")
                self.limit_type = "T"
                break
            if self.stats1["completed"]+self.stats2["completed"] >= self.sim_customer_limit:
                print("[INFO] Customer limit reached. The simulation finished successfuly.")
                self.limit_type = "C"
                break
        # self.finalize_remaining_customers()
        self.report(print_=report)

    def report(self, print_):
        """Give a report.
        """
        if self.limit_type == "C":
            total_time = self.env.now
        elif self.limit_type == "T":
            total_time = self.sim_time_limit
        completed_customers = len(self.stats1["Wait_time_in_queue"])
        avg_waiting_time_in_queue = sum(self.stats1["Wait_time_in_queue"]) / completed_customers
        avg_waiting_time_in_system = sum(self.stats1["Wait_time_in_system"]) / completed_customers
        percent_over_45 = 100 * self.stats1["Waits_more"] / completed_customers
        avg_system_length = self.stats1["Integral_of_curve"] / total_time
        utilization = self.stats1["Busy_server_time"] / total_time
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

        self.report_data1 = {"total_time": total_time,
                            "arrived":self.customer_count,
                            "served":completed_customers,
                            "wait_time_queue":avg_waiting_time_in_queue,
                            "wait_time_system":avg_waiting_time_in_system,
                            "number_system":avg_system_length}
        
        if self.limit_type == "C":
            total_time = self.env.now
        elif self.limit_type == "T":
            total_time = self.sim_time_limit
        completed_customers = len(self.stats2["Wait_time_in_queue"])
        avg_waiting_time_in_queue = sum(self.stats2["Wait_time_in_queue"]) / completed_customers
        avg_waiting_time_in_system = sum(self.stats2["Wait_time_in_system"]) / completed_customers
        percent_over_45 = 100 * self.stats2["Waits_more"] / completed_customers
        avg_system_length = self.stats2["Integral_of_curve"] / total_time
        utilization = self.stats2["Busy_server_time"] / total_time
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

        self.report_data2 = {"total_time": total_time,
                            "arrived":self.customer_count,
                            "served":completed_customers,
                            "wait_time_queue":avg_waiting_time_in_queue,
                            "wait_time_system":avg_waiting_time_in_system,
                            "number_system":avg_system_length}


