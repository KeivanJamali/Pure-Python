from modular.number_generator import Exponential_Generator, Uniform_Generator
from modular.Tools import Storage
import matplotlib.pyplot as plt


class Storage_Simulator:
    def __init__(self, demand_generator: Exponential_Generator,
                 demand_interval_generator: Uniform_Generator,
                 delay_generator: Uniform_Generator,
                 fixed_cost: float, 
                 variable_cost: float, 
                 pos_cost: float, 
                 neg_cost: float,
                 initial_level: int,
                 print_: bool = False,
                 detailed: bool = False) -> None:
        self.storage = Storage(initial_level=initial_level)
        self.demand_generator = demand_generator
        self.demand_interval_generator = demand_interval_generator
        self.delay_generator = delay_generator
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost
        self.pos_cost = pos_cost / (52 * 7) # convert the yearly cost to dayly cost.
        self.neg_cost = neg_cost / (52 * 7) # convert the yearly cost to dayly cost.
        # next send request time, next demand time, next arrive goods time.
        self.events = [[], [], []]
        self.time = 0
        self.negative_ordering_weeks = 0

    def fit(self, time_limit, policies) -> None:
        self.time_limit = time_limit # This should be days.
        for policy in policies:
            self._reset_generators()
            self.storage.reset()
            self._simulate(S=policy[0], s=policy[1], N=7) # We check the storage every 7 days.
            self._log(policy)

    def _reset_generators(self):
        self.demand_generator.reset()
        self.demand_interval_generator.reset()
        self.delay_generator.reset()

    def _simulate(self, S, s, N):
        self.S = S
        self.s = s
        self.N = N
        self._initialize()
        while True:
            event_type, event_time = self._find_event()
            self.time = event_time
            if self.time > self.time_limit:
                break
            if event_type == 0:
                self.if_send_request = self._send_request()
            elif event_type == 1:
                self._answer_to_demand()
            elif event_type == 2:
                if self.if_send_request:
                    self._get_goods()
                else:
                    self.events[2] = [self.events[2][0] + self.N, False]
            self._update_events()

    def _initialize(self) -> None:
        self.events = [[0, False],
                       [self.demand_interval_generator.next_number(), False],
                       [self.delay_generator.next_number(), False]]
        self.negative_ordering_weeks = 0

    def _find_event(self):
        current_event = min(self.events, key=lambda x: x[0])
        event_type = self.events.index(current_event)
        self.events[event_type][1] = True
        return event_type, current_event[0]

    def _send_request(self):
        if self.storage.store_level < self.s:
            request_level = self.S - self.storage.store_level
            cost = request_level * self.variable_cost + self.fixed_cost
            # print(self.events[0][0], cost)
            self.storage.spending(amount=cost)
            self.request_level = request_level
            if self.storage.store_level < 0:
                self.negative_ordering_weeks += 1
            return True
        else:
            return False
        
    def _answer_to_demand(self):
        amount_of_demand = self.demand_generator.next_number()
        self.storage.update_level(amount=-amount_of_demand, time=self.time)

    def _get_goods(self):
        self.storage.update_level(amount=self.request_level, time=self.time)

    def _update_events(self) -> None:
        if self.events[0][1]:
            self.events[0] = [self._next_send_request(), False]
        elif self.events[1][1]:
            self.events[1] = [self._next_demand(), False]
        elif self.events[2][1]:
            self.events[2] = [self._next_arrive_goods(), False]

    def _next_send_request(self):
        temp = self.events[0][0] + self.N
        return temp

    def _next_demand(self):
        temp = self.events[1][0] + self.demand_interval_generator.next_number()
        return temp

    def _next_arrive_goods(self):
        temp = self.events[0][0] + self.delay_generator.next_number()
        return temp

    def _log(self, policy):
        total_pos_cost = self.pos_cost * self.storage.integral_ip
        total_neg_cost = self.neg_cost * self.storage.integral_in
        total_spent_cost = self.storage.spent_money
        negative_days = self.storage.negative_days
        negative_ordering_weeks = self.negative_ordering_weeks
        total_days = self.time_limit
        total_weeks = total_days/7
        total_year = total_weeks/52

        print("==========================================================")
        print(f"===========policy := [ s = {policy[1]} and S = {policy[0]} ]================")
        print(f"Mean Holding costs is : {total_pos_cost/total_year}")
        print(f"Mean Shortage costs is : {-total_neg_cost/total_year}")
        print(f"Mean Order cost is : {total_spent_cost/total_year}")
        print(f"Mean Total cost is : {(total_spent_cost+total_pos_cost-total_neg_cost)/total_year}")
        print(f"Percentage of lackness weeks : {(negative_ordering_weeks)*100 / total_weeks}")
        print()

    def plot_it(self):
        temp = self.storage.initial_level
        x_values, y_values = [0], [temp]
        for x, y in self.storage.history.items():
            x_values.append(x)
            temp += y
            y_values.append(temp)
        file_name = f"storage_{self.S}_{self.s}.png"
        self.y_values = y_values
        # Plot the results
        plt.step(x_values, y_values, where='post', label="Storage Level", linewidth=2)
        plt.xlabel("Time (day)")
        plt.ylabel("Storage (Ton)")
        plt.title(f"Storage ({self.S}, {self.s})")
        plt.grid(True)
        plt.legend()
        plt.savefig(r"pics/" + file_name)
        plt.show()