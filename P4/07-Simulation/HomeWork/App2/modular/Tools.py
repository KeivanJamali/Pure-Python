class Storage:
    def __init__(self, initial_level):
        self.initial_level = initial_level
        self.store_level = self.initial_level
        self.time = 0
        self.integral_ip = 0
        self.integral_in = 0
        self.negative_weeks = 0
        self.spent_money = 0
        # can be removed
        self.history = {}

    def spending(self, amount):
        self.spent_money += amount

    def update_level(self, amount, time):
        self._integral_i(time=time)
        self.store_level += amount
        self.time = time
        # Can be removed
        self.history[time] = amount

    def _integral_i(self, time):
        x = time - self.time
        if self.store_level > 0:
            self.integral_ip += self.store_level * x
        elif self.store_level <= 0:
            self.negative_weeks += x
            self.integral_in += self.store_level * x

    def reset(self):
        self.__init__(initial_level=self.initial_level)
