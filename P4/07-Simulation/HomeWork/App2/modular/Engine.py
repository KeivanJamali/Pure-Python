from modular.number_generator import Exponential_Generator, Uniform_Generator
from modular.Tools import Storage
import matplotlib.pyplot as plt


class Storage_Simulator:
    """Storage Simulator"""

    def __init__(self, demand_generator: Exponential_Generator,
                 demand_interval_generator: Uniform_Generator,
                 delay_generator: Uniform_Generator,
                 fixed_cost: float,
                 variable_cost: float,
                 pos_cost: float,
                 neg_cost: float,
                 initial_level: int) -> None:
        """This function will simulate the storage for you.

        Args:
            demand_generator (Exponential_Generator): According to the distribution you want, you can change this useing a correct class to generate the result to you.
            demand_interval_generator (Uniform_Generator): Interval between demand.
            delay_generator (Uniform_Generator): The delay after ordering till the goods arrives.
            fixed_cost (float): Fix cost per order.
            variable_cost (float): Variable cost per ton.
            pos_cost (float): Holding cost per ton per year.
            neg_cost (float): Unmet penalty per ton per year.
            initial_level (int): The initial goods that we have in storage.
        """
        self.storage = Storage(initial_level=initial_level)
        self.demand_generator = demand_generator
        self.demand_interval_generator = demand_interval_generator
        self.delay_generator = delay_generator
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost
        # convert the yearly cost to dayly cost.
        self.pos_cost = pos_cost / (52 * 7)
        # convert the yearly cost to dayly cost.
        self.neg_cost = neg_cost / (52 * 7)
        # next send request time, next demand time, next arrive goods time, Stop time.
        self.events = [[], [], [], []]
        self.time = 0
        self.negative_ordering_weeks = 0

    def fit(self, time_limit:int, policies:list) -> None:
        """THis function will fit the data and run the simulator.

        Args:
            time_limit (int): Time limit in day.
            policies (list): [[S1, s1], [S2, s2], ...]
        """
        self.time_limit = time_limit  # This should be days.
        for policy in policies:
            self._reset_generators()
            self.storage.reset()
            # We check the storage every 7 days.
            self._simulate(S=policy[0], s=policy[1], N=7)
            self._log(policy)

    def _reset_generators(self) -> None:
        """This function will reset all generators to help you compare different policies(regenerating).
        """
        self.demand_generator.reset()
        self.demand_interval_generator.reset()
        self.delay_generator.reset()

    def _simulate(self, S:int, s:int, N:int) -> None:
        """According to S and s and the N the simulation will start.

        Args:
            S (int): Max capacity at storage.
            s (int): Minimum acceptable level at storage.
            N (int): At what days will we check the storage?(for example: 7(days) means we check each week.)
        """
        self.S = S
        self.s = s
        self.N = N
        self._initialize()
        while True:
            event_type, event_time = self._find_event()
            self.time = event_time

            if event_type == 0:
                self.if_send_request = self._send_request()
            elif event_type == 1:
                self._answer_to_demand()
            elif event_type == 2:
                if self.if_send_request:
                    self._get_goods()
                else:
                    self.events[2] = [self.events[2][0] + self.N, False]
            elif event_type == 3:
                self.storage.update_level(amount=0, time=self.time)
                break
            self._update_events()

    def _initialize(self) -> None:
        """Set the initial state for us. Put negative ordering weeks parameter to 0.
        """
        self.events = [[0, False],
                       [self.demand_interval_generator.next_number(), False],
                       [self.delay_generator.next_number(), False],
                       [self.time_limit, False]]
        self.negative_ordering_weeks = 0

    def _find_event(self)-> tuple:
        """Tell us the next event.

        Returns:
            tuple: (type of the event, time of the event)
        """
        current_event = min(self.events, key=lambda x: x[0])
        event_type = self.events.index(current_event)
        self.events[event_type][1] = True
        return event_type, current_event[0]

    def _send_request(self) -> bool:
        """THis function will check the storage.

        Returns:
            bool: True if we order some goods, False if the storage level is more than our limit(s).
        """
        if self.storage.store_level < self.s:
            request_level = self.S - self.storage.store_level
            self.cost = request_level * self.variable_cost + self.fixed_cost
            self.request_level = request_level
            if self.storage.store_level < 0:
                self.negative_ordering_weeks += 1
            return True
        else:
            return False

    def _answer_to_demand(self) -> None:
        """When we have a demand this function will answer to it.
        """
        amount_of_demand = self.demand_generator.next_number()
        self.storage.update_level(amount=-amount_of_demand, time=self.time)

    def _get_goods(self) -> None:
        """Recieve the goods when they arrive.
        """
        self.storage.update_level(amount=self.request_level, time=self.time)
        self.storage.spending(amount=self.cost)

    def _update_events(self) -> None:
        """This function will update the list of events. It works in each iteration.
        """
        if self.events[0][1]:
            self.events[0] = [self._next_send_request(), False]
        elif self.events[1][1]:
            self.events[1] = [self._next_demand(), False]
        elif self.events[2][1]:
            self.events[2] = [self._next_arrive_goods(), False]

    def _next_send_request(self) -> float:
        """Generate the time for next check.

        Returns:
            float: time
        """
        temp = self.events[0][0] + self.N
        return temp

    def _next_demand(self) -> float:
        """Generate the time for next deman.

        Returns:
            float: time
        """
        temp = self.events[1][0] + self.demand_interval_generator.next_number()
        return temp

    def _next_arrive_goods(self) -> float:
        """Tell us the next time that goods will arrive.

        Returns:
            float: time
        """
        temp = self.events[0][0] + self.delay_generator.next_number()
        return temp

    def _log(self, policy:list) -> None:
        """This function will print the information and metrics we want.

        Args:
            policy (list): (S, s)
        """
        total_pos_cost = self.pos_cost * self.storage.integral_ip
        total_neg_cost = self.neg_cost * self.storage.integral_in
        total_spent_cost = self.storage.spent_money
        negative_days = self.storage.negative_days
        negative_ordering_weeks = self.negative_ordering_weeks
        total_days = self.time_limit
        total_weeks = total_days/7
        total_year = total_weeks/52

        holding = round(total_pos_cost/total_year, 1)
        shortage = -round(total_neg_cost/total_year, 1)
        order = round(total_spent_cost/total_year, 1)
        total = round((total_spent_cost + total_pos_cost -
                      total_neg_cost) / total_year, 1)

        print("==========================================================")
        print(
            f"===========policy := [ s = {policy[1]} and S = {policy[0]} ]================")
        print(f"Mean Holding costs is : {holding}")
        print(f"Mean Shortage costs is : {shortage}")
        print(f"Mean Order cost is : {order}")
        print(f"Mean Total cost is : {total}")
        print(
            f"Percentage of lackness weeks : {(negative_ordering_weeks)*100 / total_weeks}")
        print()

    def plot_it(self) -> None:
        """This function visulaze the storage history.
        """
        temp = self.storage.initial_level
        x_values, y_values = [0], [temp]
        for x, y in self.storage.history.items():
            x_values.append(x)
            temp += y
            y_values.append(temp)
        file_name = f"storage_{self.S}_{self.s}.png"
        self.y_values = y_values
        # Plot the results
        plt.step(x_values, y_values, where='post',
                 label="Storage Level", linewidth=2)
        plt.xlabel("Time (day)")
        plt.ylabel("Storage (Ton)")
        plt.title(f"Storage ({self.S}, {self.s})")
        plt.grid(True)
        plt.legend()
        plt.savefig(r"pics/" + file_name)
        plt.show()
