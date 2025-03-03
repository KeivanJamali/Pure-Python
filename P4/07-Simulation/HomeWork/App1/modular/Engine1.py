from modular.number_generator import Exponential_Generator
from modular.Tools import Queue, Server, System
import matplotlib.pyplot as plt
import time


class Simulator_FCFS:
    def __init__(self, interval_generator:Exponential_Generator, 
                 service_time_generator:Exponential_Generator,
                 sleep=3,
                 print_=False,
                 detailed=False):
        self.print_ = print_
        self.detailed = detailed
        self.interval_generator = interval_generator
        self.service_time_generator = service_time_generator
        self.intervals = []
        self.service_times = []
        self.arrivals = []
        self.departures = []
        self.interval_counter = -1
        self.service_time_counter = -1
        self.queue = Queue()
        self.server = Server()
        self.system = System()
        self.time = 0
        self.last_event = None
        self.last_id = 0
        self.number_of_ids = 0
        self.left_over_queue = []
        self.left_over_system = []

    def fit(self, policy, last_id=float("inf"), last_time=float("inf")):
        if last_id < 3:
            raise ValueError("[ERROR] You must set at least 3 id arrive in system.")
        self.stop_id, self.stop_time = last_id, last_time

        if policy=="FCFS":
            self.FCFS()
        elif policy=="SPT":
            self.SPT()
        else:
            raise ValueError("[ERROR] You must chose the model correctly.")
        
    def FCFS(self):
        again = True
        self._next_arrival()
        while again:
            self._initialize(id_=self.arrivals[-1][0], time=self.arrivals[-1][1], type_="AD")
            self._visulize(detailed=self.detailed)
            while True:
                self._find_next_event_with_FCFS_policy()
                id_, time, type_ = self._decide_on_arrival_or_departure()
                result = self._check_and_update(id_, time, type_)
                self._visulize(detailed=self.detailed) 
                if result[0]:
                    again = False
                    break

                if result[1] == 2:
                    again = True
                    # self.queue.time_in_queue.pop()
                    break

    def _initialize(self, id_, time, type_):
        self.queue.arrive(id_, time)
        self.system.arrive(id_, time)
        self.queue.depart(id_, time)
        self.server.occupied_at(id_, time)
        self.number_of_ids += 1
        self._update_id_and_time_and_event(id_=id_, time=time, type_=type_)


    def _stop_check(self, id_, time, type_):
        if id_ == self.stop_id-1 and type_ == "D":
            self._update_id_and_time_and_event(id_, time, type_)
            self._eos_id()
            self._log(last=True, detailed=self.detailed)
            return True
        if time >= self.stop_time:
            self._eos_time(self.stop_time)
            self._log(last=True, detailed=self.detailed)
            return True
        return False

    def _eos_id(self):
        self.left_over_queue = self.queue.queue[:]
        for id_ in self.left_over_queue:
            self.queue.depart(id_, self.time)
        if self.server.occupied:
            self.server.unoccupied_at(self.time)
        self.left_over_system = self.system.queue[:]
        for id_ in self.left_over_system:
            self.system.depart(id_, self.time)

    def _eos_time(self, time):
        self.left_over_queue = self.queue.queue[:]
        for id_ in self.left_over_queue:
            self.queue.depart(id_, time)
        if self.server.occupied:
            self.server.unoccupied_at(time)
        self.left_over_system = self.system.queue[:]
        for id_ in self.left_over_system:
            self.system.depart(id_, time)

    def _find_next_event_with_FCFS_policy(self):
        if "A" in self.last_event:
            self._next_arrival()
        if "D" in self.last_event:
            self._next_service_time()

    def _next_arrival(self):
        self.interval_counter += 1
        self.intervals.append([self.interval_counter, self.interval_generator.next_number()])
        temp = sum(i[1] for i in self.intervals)
        self.arrivals.append([self.interval_counter, temp])

    def _next_service_time(self):
        self.service_time_counter += 1
        self.service_times.append([self.service_time_counter, self.service_time_generator.next_number()])

    def _decide_on_arrival_or_departure(self) -> tuple:
        if "D" in self.last_event:
            temp = max(self.time, self.departures[-1][0]) if self.departures else self.time
            self.departures.append([self.service_times[-1][0], temp + self.service_times[-1][1]])
        if self.arrivals[-1][1] < self.departures[-1][1]:
            return (self.arrivals[-1][0], self.arrivals[-1][1], "A")
        else:
            return (self.departures[-1][0], self.departures[-1][1], "D")

    def _update_id_and_time_and_event(self, id_, time, type_) -> None:
        self.time = time
        self.last_id = id_
        self.last_event = type_
        if self.number_of_ids <= self.last_id:
            self.number_of_ids = self.last_id + 1

    def _update_system(self, id_, time, type_):
        if type_ == "A":
            self.queue.arrive(id_, time)
            self.system.arrive(id_, time)
            return (False, 0)

        elif type_ == "D":
            self.system.depart(id_, time)
            if len(self.queue) > 0:
                self.queue.depart(id_+1, time)
                self.server.occupied_at(id_+1, time)
                return (False, 1)
            else:
                self.server.unoccupied_at(time)
                self.departures[-1] = (self.departures[-1][0], self.arrivals[-1][1])
                return (False, 2)

    def _check_and_update(self, id_, time, type_):
        if self._stop_check(id_, time, type_):
            return (True, 0)
        else:
            result = self._update_system(id_, time, type_)
            self._update_id_and_time_and_event(id_, time, type_)
            return result

            
    def plot_sample_path(self):
        # Extract unique time points
        time_points = sorted(set(time for interval in self.system.history.values() for time in interval))
        if time_points[0] != 0:
            time_points.insert(0, 0)

        # Count the number of people in the system at each time point
        people_count = []
        for t in time_points:
            count = sum(start <= t < end for start, end in self.system.history.values())
            people_count.append(count)

        # Plot the results
        plt.step(time_points, people_count, where='post', label="People in System", linewidth=2)
        plt.xlabel("Time")
        plt.ylabel("Number of People")
        plt.title("People in System Over Time")
        plt.grid(True)
        plt.legend()
        plt.show()


    def _log(self, last=False, detailed=False):
        try:
            Q_bar = self.queue.time_in_queue[self.departures[-1][0]]/(len(self.departures))
        except:
            Q_bar = "First time"
        total_time = self.server.occupied_time+self.server.unoccupied_time
        N_Q = self.queue.time_in_queue[-1]/total_time
        U = self.server.occupied_time/total_time
        N = N_Q + U
        print("=======================================================")
        if not last:
            print(f"We are at time {self.time} talking about person {self.last_id} to '{self.last_event}'")
        if not last and detailed:
            print(f"intervals: {self.intervals}")
            print(f"service_times: {self.service_times}")
            print(f"Arrival: {self.arrivals}")
            print(f"Departures: {self.departures}")
        if detailed:
            print(f"Our Queue is {self.left_over_queue} currently.")
            print(f"Our server is occupied({self.server.occupied}).")
            print()
            print(f"Statistical Parameter:")
            print(f"For our queue we have this history:   ", end="")
            print(self.queue.history)
            print(f"For our server we have this history:   ", end="")
            print(self.server.history)
            print(f"For our system we have this history:   ", end="")
            print(self.system.history)
            print(f"Occupied time for server is {self.server.occupied_time} and the rest ({self.server.unoccupied_time}) is unoccupied.")
            print(f"Total time in queue is {self.queue.time_in_queue} -> {self.queue.time_in_queue[self.departures[-1][0]]}") if self.departures else 0
        print()
        print(f"Therefore the U={U}")
        print(f"We have {self.system.count_45_min_id} people with more that 4.5 min system time. Therefore the percentage is {100*self.system.count_45_min_id/self.number_of_ids}")
        print(f"Therefore, Average Number of People in Queue (N_Q) will be {N_Q}")
        print(f"Therefore, Average Wating time for People in Queue (Q_bar) will be {Q_bar}")
        print(f"Therefoe, Average Number of People in System (N) will be {N}")
        print()
        print("=======================================================")        

    def _visulize(self, last=False, detailed=False):
        if self.print_:
            self._log(last=last, detailed=detailed)
