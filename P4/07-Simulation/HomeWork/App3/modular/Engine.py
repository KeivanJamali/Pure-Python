import simpy as si
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Customer:
    def __init__(self, cid:int, interval_time:float, service_time:float, queue:object=None):
        self.cid = cid
        self.interval_time = interval_time
        self.service_time = service_time
        self.queue = queue
        self.arrival_time = None
        self.env = None
        self.resource = None
        self.start_service = None
        self.finish_service = None
        self.action = None

    def add_to_env(self, env:si.Environment, resource:si.Resource):
        self.env = env
        self.resource = resource
    
    def start_action(self):
        self.action = self.env.process(self._process())

    def _process(self):
        self.arrival_time = self.env.now
        with self.resource.request() as request:
            yield request
            self.start_service = self.env.now
            yield self.env.timeout(delay=self.service_time)
            self.finish_service = self.env.now
            if self.queue:
                self.queue.history["done_customers"].append(self.cid)


class Queue:
    def __init__(self, interval_gen:object, service_time_gen:object):
        self.interval_gen = interval_gen
        self.service_time_gen = service_time_gen
        self.end_time = [None, None] # [Time, Done_Customers]
        self.end_by_time = False
        self.now = None

        self.env = si.Environment(initial_time=0)
        self.resource = si.Resource(self.env, capacity=1)
        self.done_event = self.env.event()

        self.customers = {}
        self.history = {"arrived_customers":[],
                        "done_customers":[]}
        
        self.stats = {"average_queue_waiting_time":None,
                      "average_queue_length":None,
                      "server_utility":None,
                      "waited_more_than_45min_in_system":None}
        
    def _fcfs_process(self):
        cid = -1
        while True:
            cid += 1
            interval = self.interval_gen()
            service_time = self.service_time_gen()
            yield self.env.timeout(delay=interval)

            self.history["arrived_customers"].append(cid)
            customer = Customer(cid=cid, interval_time=interval, service_time=service_time, queue=self)
            self.customers[cid] = customer
            customer.add_to_env(self.env, resource=self.resource)
            customer.start_action()
            
            if self.env.now >= self.end_time[0]:
                print(f"[Success] Finished at time {self.end_time[0]} (next_event={self.env.now})")
                self.end_by_time = True
                self.now = self.env.now
                self.history["arrived_customers"].pop()
                self.done_event.succeed()
            
            elif len(self.history["done_customers"]) >= self.end_time[1]:
                print(f"[Success] Finished by the last customer= {self.history['done_customers'][-1]} with total {self.end_time[1]} customers done job.")
                self.end_by_time = False
                self.now = self.env.now
                self.done_event.succeed()

    def run(self, queue_type:str, time_limit:float=None, customer_limit:int=None):
        self.end_time = [time_limit, customer_limit]
        if queue_type == "FCFS":
            print(f"[INFO] Starting the simulation...")
            self.env.process(self._fcfs_process())
            self.env.run(until=self.done_event)
            
    def analysis(self):
        # average queue wating time = p1
        # average queue length = p2
        # average system length = p3
        # number of more waited people = p4
        total_p1 = 0
        total_p2 = 0
        total_p3 = 0
        total_p4 = 0
        for cid in self.history["arrived_customers"]:
            if self.customers[cid].start_service:
                if self.customers[cid].finish_service:
                    total_p1 += self.customers[cid].start_service - self.customers[cid].arrival_time
                    total_p2 += self.customers[cid].start_service - self.customers[cid].arrival_time
                    total_p3 += self.customers[cid].start_service - self.customers[cid].arrival_time + self.customers[cid].service_time
                    if self.customers[cid].start_service - self.customers[cid].arrival_time + self.customers[cid].service_time > 4.5:
                        total_p4 += 1
                else:
                    total_p2 += self.customers[cid].start_service - self.customers[cid].arrival_time
                    if self.end_by_time:
                        total_p3 += self.end_time[0] - self.customers[cid].arrival_time
                        if self.end_time[0] - self.customers[cid].arrival_time > 4.5:
                            total_p4 += 1
                    else:
                        total_p3 += self.now - self.customers[cid].arrival_time
                        if self.now - self.customers[cid].arrival_time > 4.5:
                            total_p4 += 1
            else:
                if self.end_by_time:
                    total_p2 += self.end_time[0] - self.customers[cid].arrival_time
                    total_p3 += self.end_time[0] - self.customers[cid].arrival_time
                    if self.end_time[0] - self.customers[cid].arrival_time > 4.5:
                        total_p4 += 1
                else:
                    total_p2 += self.now - self.customers[cid].arrival_time
                    total_p3 += self.now - self.customers[cid].arrival_time
                    if self.now - self.customers[cid].arrival_time > 4.5:
                        total_p4 += 1

        p1 = total_p1 / len(self.history["done_customers"])
        if self.end_by_time:
            p2 = total_p2 / self.end_time[0]
            p3 = total_p3 / self.end_time[0]
        else:
            p2 = total_p2 / self.now
            p3 = total_p3 / self.now
        p4 = total_p4 / len(self.history["arrived_customers"])
        print(total_p4)

        self.stats["average_queue_waiting_time"] = p1
        self.stats["average_queue_length"] = p2
        self.stats["server_utilization"] = p3 - p2
        self.stats["waited_more_than_45min_in_system"] = p4

        
    def summary(self):
        print(f"\n----- Simulation Report/summary -----")
        print(f"Total done customers: {len(self.history['done_customers'])}")
        print(f"Total arrived customers: {len(self.history['arrived_customers'])}")
        print(f"Average wait time in queue: {self.stats['average_queue_waiting_time']:.2f}")
        print(f"Average length of queue: {self.stats['average_queue_length']:.2}")
        print(f"Server utilization: {100 * self.stats['server_utilization']:.2f}%")
        print(f"Percent of customers who waited more than 4.5min: {100 * self.stats['waited_more_than_45min_in_system']:.2f}%")
        print(f"Simulation ended at time: {self.now:.2f}")
        print(f"-------------------------------------")


