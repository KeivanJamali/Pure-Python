from modular_old.number_generator import Exponential_Generator
from modular_old.Tools import Queue, Server, System
import matplotlib.pyplot as plt
import time


class Queue_Simulator:
    """Simulating a one server one queue system using two seprate algorithm for FirstComeFirstServe(FCFS) and ShortestProcessingTimeFirst(SPT).
    """
    def __init__(self, interval_generator:Exponential_Generator,
                 service_time_generator:Exponential_Generator,
                 print_:bool=False,
                 detailed:bool=False) -> None:
        """Important parameters:
           1- intervals, service_times, arrivals, departures: Storing lists for events.
           2- Queue, Server, System: Classes we definded for this class.
           3- last_id, time, last_event: Main step parameters to observe the condition in system.

        Args:
            interval_generator (Exponential_Generator): A generator to make intervals for adding to system.
            service_time_generator (Exponential_Generator): A generator to make service times of the people in the system.
            print_ (bool, optional): If you want to have the informatino in each step to be printed. Defaults to False.
            detailed (bool, optional): If you want to have some more deep informatino about the system. Defaults to False.
        """
        self.print_ = print_
        self.detailed = detailed
        self.interval_generator = interval_generator
        self.service_time_generator = service_time_generator
        self.intervals = []
        self.service_times = []
        self.service_times_copy = []
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
        self.policy = None

    def fit(self, policy:str, last_id:float=float("inf"), last_time:float=float("inf")) -> None:
        """Run the algorithm for the simulation.

        Args:
            policy (str): 'FCFS' or 'SPT'.
            last_id (float, optional): If you know the last person id in the system to stop the simulation. Defaults to float("inf").
            last_time (float, optional): If you knwo the last time that the simulation should continue the run to. Defaults to float("inf").

        Raises:
            ValueError: The minimum value for last_id is 3.
            ValueError: You must set policy to 'FCFS' or 'SPT'. Nothing else.
        """
        self.policy = policy
        if last_id < 3:
            raise ValueError("[ERROR] You must set at least 3 id arrive in system.")
        self.stop_id, self.stop_time = last_id, last_time

        if policy=="FCFS":
            self._FCFS()
        elif policy=="SPT":
            self._SPT()
        else:
            raise ValueError("[ERROR] You must chose the policy correctly.")
        
    def _FCFS(self):
        """Run the simulation with the FCFS policy ( First come First serve ).\n
        1- Starts with the first person enter the system.\n
        2- If the server starts from unoccupied condition, Initializing will happen.\n
        3- Then the next event will be chosen according to the policy.\n
        4- System and all the metrics will be updated accordingly.\n
        5- If the time or last person criteria comes, the code will stop and print the metrics at the end.
        """
        again = True
        self._next_arrival()
        while again:
            self._initialize(id_=self.arrivals[-1][0], time=self.arrivals[-1][1])
            self._visulize(detailed=self.detailed)
            while True:
                self._find_next_event_with_FCFS_policy()
                id_, time, type_ = self._decide_on_arrival_or_departure_FCFS()
                result = self._check_and_update(id_, time, type_)
                self._visulize(detailed=self.detailed)

                if result[0]:
                    again = False
                    break

                if result[1] == 2:
                    again = True
                    break

    def _SPT(self) -> None:
        """Run the simulation with the SPT policy ( Shortest Processing Time First )\n
        1- Starts with the first person enter the system.\n
        2- If the server starts from unoccupied condition, Initializing will happen.\n
        3- Then the next event will be chosen according to the policy.\n
        4- System and all the metrics will be updated accordingly.\n
        5- If the time or last person criteria comes, the code will stop and print the metrics at the end.
        """
        again = True
        self._next_arrival()
        while again:
            self._initialize(id_=self.arrivals[-1][0], time=self.arrivals[-1][1])
            self._visulize(detailed=self.detailed)
            while True:
                self._find_next_event_with_SPT_policy()
                id_, time, type_ = self._decide_on_arrival_or_departure_SPT()
                result = self._check_and_update(id_, time, type_)
                self._visulize(detailed=self.detailed) 
                if result[0]:
                    again = False
                    break

                if result[1] == 2:
                    again = True
                    break

    def _initialize(self, id_:int, time:float, type_:str="AD") -> None:
        """Initialize the system by entering the first person to the [system, queue, server] and exiting the [queue] immediately.

        Args:
            id_ (int): The id of the person who is the one who will start the system.
            time (float): What time do you want to start the system at?
            type_ (str): The condition to start whcih is always 'AD'. which means that we need both 'A'=Arrival and 'D'=Departure. Defaults to 'AD'.
        """
        self.queue.arrive(id_, time)
        self.system.arrive(id_, time)
        self.queue.depart(id_, time)
        self.server.occupied_at(id_, time)
        self.number_of_ids += 1
        self._update_id_and_time_and_event(id_=id_, time=time, type_=type_)

    def _stop_check(self, id_:int, time:float, type_:str) -> bool:
        """Check to see if any of the criteria ( last id or last time ) happens or not.\n
        1- If the last id comes first, we also check that this person is departing from the system ( At time when the last person leave the system ); and call the eos for last id.\n
        2- If the last time critera comes first, we run the eos for time.
        
        Args:
            id_ (int): The id that the current person has.
            time (float): the time that we are currently processing at.
            type_ (str): Additional information about the person condition. If he is arriving at system='A' or if he is departing from the system='D'.

        Returns:
            bool: If the system should stop it will return True, else -> False.
        """
        if len(self.departures) == self.stop_id and type_ == "D":
            self._update_id_and_time_and_event(id_, time, type_)
            self._eos_id()
            self._log(last=True, detailed=self.detailed)
            return True

        if time >= self.stop_time:
            self.departures.pop()
            self._eos_time(self.stop_time)
            self._log(last=True, detailed=self.detailed)
            return True
        return False

    def _eos_id(self) -> None:
        """It will exit all the people in the system to calculate their waiting time and all other metrics we want, while store the data of people who are still in the system.
        """
        self.left_over_queue = self.queue.queue[:]
        for id_ in self.left_over_queue:
            self.queue.depart(id_, self.time)
        if self.server.occupied:
            self.server.unoccupied_at(self.time)
        else:
            self.server.occupied_at(id="eos", time=self.time)
        self.system.depart(self.last_id, self.time)
        self.total_time = self.time

    def _eos_time(self, time:float) -> None:
        """It will exit all the people in the sytem to calculate their waiting time and all other metrics we want, while store the data of people who are still in the system.

        Args:
            time (float): The last time for the last event. This time can be diffrent from the last time.
        """
        self.left_over_queue = self.queue.queue[:]
        for id_ in self.left_over_queue:
            self.queue.depart(id_, time)
        if self.server.occupied:
            self.server.unoccupied_at(time)
        self.server.check_correction(time)
        self.total_time = time


    def _find_next_event_with_FCFS_policy(self) -> None:
        """If the last event is arrival, then the system should find the next arrival,\n
           If the last event is departure, then the system should find the next departure,\n
           This works only for FCFS policy.
        """
        if "A" in self.last_event:
            self._next_arrival()
        if "D" in self.last_event:
            self._next_service_time()

    def _find_next_event_with_SPT_policy(self) -> None:
        """If and only if the last event is arrival, the system will generate the new arrival and departure.\n
           This works only for SPT policy.
        """
        if "A" in self.last_event:
            self._next_arrival()
            self._next_service_time()

    def _next_arrival(self) -> None:
        """In this function we will use the generator to add the next person who is added to the system.\n
           We will add it to the intervals and arrivals list. Each member: [person_id, time]
        """
        self.interval_counter += 1
        self.intervals.append([self.interval_counter, self.interval_generator()])
        temp = sum(i[1] for i in self.intervals)
        self.arrivals.append([self.interval_counter, temp])

    def _next_service_time(self) -> None:
        """In this function we will use the generator to add the time of processing each person needs ( This time is for the i-1 person ).
           We will add it to the service_time_times. Each member: [person_id, time].
        """
        self.service_time_counter += 1
        self.service_times.append([self.service_time_counter, self.service_time_generator()])
        self.service_times_copy.append([self.service_time_counter, self.service_times[-1][1]])


    def _decide_on_arrival_or_departure_FCFS(self) -> tuple[int, float, str]:
        """In the FCFS policy, we should decide if the next event is arrival or departure.\n
           1- If the last event is departure, that means we need to calculate the next depature time first which is:\n
           The person service time + max(current time and the departure of the previous person.)\n
           2- If the last event is arrival, we use the departure time that we calculated before.\n
           3- We chose the earlier time and return the information about that person, time, and type(A, D)

        Returns:
            tuple[int, float, str]: person_id, time, type of event.
        """
        if "D" in self.last_event:
            temp = max(self.time, self.departures[-1][0]) if self.departures else self.time
            self.departures.append([self.service_times[-1][0], temp + self.service_times[-1][1]])
        if self.arrivals[-1][1] < self.departures[-1][1]:
            return (self.arrivals[-1][0], self.arrivals[-1][1], "A")
        else:
            return (self.departures[-1][0], self.departures[-1][1], "D")
        
    def _decide_on_arrival_or_departure_SPT(self) -> tuple[int, float, str]:
        """In the SPT policy, we should decide if the next event is arrival or departure.\n
           1- If the last event is departure, that means we need to caluclate the next departure time first which is:\n
           The person with minimum service time + max(current time and the departure of the previous person.)\n
           2- If the last event is arrival, we use the departure time that we calculated before.\n
           3- We chose the earlier time and return the information about that person, time, and type(A, D).

        Returns:
            tuple[int, float, str]: person_id, time, type of event.
        """
        if "D" in self.last_event:
            id_departure, min_service_time = min(self.service_times, key=lambda x: x[1])
            temp = max(self.time, self.departures[-1][1]) if self.departures else self.time
            self.id_departure, self.time_departure = id_departure, temp + min_service_time
            self.min_service_time = min_service_time
            self.departures.append([self.id_departure, self.time_departure])
        if self.arrivals[-1][1] < self.time_departure:
            return (self.arrivals[-1][0], self.arrivals[-1][1], "A")
        else:
            return (self.id_departure, self.time_departure, "D")

    def _update_id_and_time_and_event(self, id_:int, time:float, type_:str) -> None:
        """This function will only update the current system information which is person_id, time and type of the last event.

        Args:
            id_ (int): Id of the person.
            time (float): Time.
            type_ (str): A=arrival or D=Departure.
        """
        self.time = time
        self.last_id = id_
        self.last_event = type_
        if self.number_of_ids <= self.last_id:
            self.number_of_ids = self.last_id + 1

    def _update_system_FCFS(self, id_:int, time:float, type_:str) -> tuple[bool, int]:
        """This function will update the system according to the id, time and type that it received. It only works for FCFS policy.\n
           1- If event type is Arrival, the person in time will be added to system and queue. Returns (False, 0).\n
           2- If event type is Departure and we have still some people at queue,\n
           it will remove the ith person from system, (i+1)th person from queue and occupy the server by (i+1)th person. Returns (False, 1).\n
           3- If event type is Departure and we have no other person in the queue,\n
           it will unoccupy the sever and remove the ith person from the system. It will also move the last departure time to the last arrival time.\n
           This is because the system now is empty and therefore when we take the max(current time and last departure time) we need to have the last arrival time in this scenario.\n
           To make this happens, it is necessary to make this update for the logic of the code. Returns (False, 2).\n

        Args:
            id_ (int): Person Id.
            time (float): Time.
            type_ (str): A=arrival or D=departure.

        Returns:
            tuple[bool, int]: [If the system should stop, number of the type of update happend in the system.]
        """
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
                self.departures[-1] = [self.departures[-1][0], self.arrivals[-1][1]]
                return (False, 2)

    def _update_system_SPT(self, id_:int, time:float, type_:str) -> None:
        """This function will update the system according to the id, time and type that it received. It only works for SPT policy.\n
           1- If event type is Arrival, the person in time will be added to system and queue. Returns (False, 0).\n
           2- If event type is Departure and we have still some people at queue,\n
           it will remove the ith person from system, the person with shortest service time from queue and occupy the server with that person. Returns (False, 1).\n
           3- If event type is Departure and we have no other person in the queue,\n
           it will unoccupy the sever and remove the ith person from the system. It will also move the last departure time to the last arrival time.\n
           This is because the system now is empty and therefore when we take the max(current time and last departure time) we need to have the last arrival time in this scenario.\n
           To make this happens, it is necessary to make this update for the logic of the code. Returns (False, 2).\n

        Args:
            id_ (int): Person Id.
            time (float): Time.
            type_ (str): A=arrival or D=departure.

        Returns:
            tuple[bool, int]: [If the system should stop, number of the type of update happend in the system.]
        """
        if type_ == "A":
            self.queue.arrive(id_, time)
            self.system.arrive(id_, time)
            return (False, 0)

        elif type_ == "D":
            self.system.depart(id_, time)
            self.service_times.remove([self.id_departure, self.min_service_time])
            if len(self.queue) > 0:
                id_temp = min(self.service_times, key=lambda x: x[1])[0]
                self.queue.depart(id_temp, time)
                self.server.occupied_at(id_temp, time)
                return (False, 1)
            else:
                self.server.unoccupied_at(time)
                self.departures[-1] = [self.departures[-1][0], self.arrivals[-1][1]]
                return (False, 2)

    def _check_and_update(self, id_:int, time:float, type_:str) -> tuple[bool, int]:
        """This function will update the system by considering everything all together.\n
           1- It will check if the system should stop or not. If yes returns (True, 0).\n
           2- Check the policy and call the update function and update the 3 main parametert in the code ( id, time, type ).\n

        Args:
            id_ (int): Person id.
            time (float): Time.
            type_ (str): A=arrival or D=departure.

        Returns:
            tuple[bool, int]: [If the system should stop, What type of update happend to the system.]
        """
        if self._stop_check(id_, time, type_):
            return (True, 0)
        else:
            if self.policy == "FCFS":
                result = self._update_system_FCFS(id_, time, type_)
            elif self.policy == "SPT":
                result = self._update_system_SPT(id_, time, type_)
            self._update_id_and_time_and_event(id_, time, type_)
            return result

            
    def plot_sample_path(self, file_name="default.png") -> None:
        """Plot the sample path. This function is only for some visualization. Read the data from system history.
        """
        # Extract unique time points
        time_points = sorted(set(time for interval in self.system.history.values() for time in interval))
        if time_points[0] != 0:
            time_points.insert(0, 0)
        if self.stop_time<10**10:
            last = time_points.pop()
            time_points.append(last)

        # Count the number of people in the system at each time point
        people_count = []
        dummy_end_time = self.stop_time if self.stop_time<10**10 else max(time_points) + 1
        for t in time_points:
            count = sum(start <= t < (end if len(times) > 1 else dummy_end_time) 
                for times in self.system.history.values()
                for start, *end_list in [times]  # Unpack arrival & optional departure
                for end in (end_list if end_list else [None]))
            people_count.append(count)
        
        # last person in time.
        if self.stop_time<10**10:
            time_points.append(self.stop_time)
            people_count.append(people_count[-1])

        # Plot the results
        plt.step(time_points, people_count, where='post', label="People in System", linewidth=2)
        plt.xlabel("Time")
        plt.ylabel("Number of People")
        plt.title("People in System Over Time")
        plt.grid(True)
        plt.legend()
        plt.savefig(r"pics/" + file_name)
        plt.show()


    def _log(self, last:bool=False, detailed:bool=False) -> None:
        """This function will print all the information about system accordin to the needs.\n
           1- Calculate Q_bar: Time in queue of the last person who departe from the system during / number of people who successfully departe from the system.\n
           2- Calculate total time: sum(time of occupation for server + time of unoccupied for server).\n
           3- Calculate N_Q: Total time in queue ( Area under the sample path plot ) / total time of simulation.\n
           4- Calculate U: Occupied time of the system / total time of simulation.\n
           5- Calculate N: Sumation of N_Q and U.

        Args:
            last (bool, optional): If we are in the last step, this way it won't write the id or some microscopic information. Defaults to False.
            detailed (bool, optional): Write down all the details in steps. Defaults to False.
        """
        try:
            temp_id = max(self.departures, key=lambda x: x[1])[0]
            time_in_queue = next((i for i in self.queue.time_in_queue if i[0] == temp_id), None)[1]
            Q_bar = time_in_queue/len(self.departures)
        except:
            time_in_queue = 0
            Q_bar = 0

        total_time = self.stop_time if self.stop_time < 10**10 else self.time
        total_time_in_queue = self.queue.total_time_in_queue
        N_Q = total_time_in_queue/total_time
        # Occupied time = sum(service_times)
        # temp = [[key, value] for key, _ in self.departures for k, value in self.service_times_copy if k == key]
        # temp = sum(i[1] for i in temp)
        # U2 = temp / total_time

        U = self.server.occupied_time / self.server.total_time


        people_45 = 100*self.system.count_45_min_id/len(self.departures) if self.departures else 1
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
            print(f"Occupied time for server is {self.server.occupied_time} and the rest ({self.server.total_time}) is unoccupied.")
            if self.policy == "FCFS":
                print(f"Total time in queue is {self.queue.time_in_queue} -> {time_in_queue}") if self.departures else 0
            elif self.policy == "SPT":
                print(f"Total time in queue is {self.queue.time_in_queue} -> {time_in_queue}") if self.departures else 0
        print()
        print(f"Therefore, Average waiting time for People in Queue (Q_bar) will be {Q_bar:.2f}")
        print(f"Therefore, Average number of People in Queue (N_Q) will be {N_Q:.2f}")
        print(f"We have {self.system.count_45_min_id} people with more that 4.5 min system time. Therefore the percentage is {people_45:.2f}")
        print(f"Therefore the U={U*100:.2f}")
        # print(f"Therefore the U={U2*100:.2f}")
        # print(f"Therefore, Average Number of People in System (N) will be {N}")
        print()
        print("=======================================================")
        data = {
            "clock": self.time,
            "server_status": self.server.occupied,
            "queue_times": self.queue.queue,
            "stats": {
                "Average Wating Time (Q_Bar)": Q_bar,
                "Average Number of People in Queue (N_Q)": N_Q,
                "Percentage of people who were in the system more than 4.5 min": people_45,
                "U": U
            }
        }
        return data

    def _visulize(self, last:bool=False, detailed:bool=False) -> None:
        """This function will call the log function if the system variable self.print_ is True.

        Args:
            last (bool, optional): If we are in the last step, this way it won't write the id or some microscopic information.. Defaults to False.
            detailed (bool, optional): Write down all the details in steps. Defaults to False.. Defaults to False.
        """
        if self.print_:
            self._log(last=last, detailed=detailed)
