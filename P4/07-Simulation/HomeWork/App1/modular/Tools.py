class Queue:
    """Simulate the queue.
    """
    def __init__(self):
        """Parameters:\n
           1- queue: People id in the queue.\n
           2- history: {id: [time of entering the queue, time of leaving the queue]}\n
        """
        self.queue = []
        self.history = {}
        self.time_in_queue = []

    def arrive(self, id:str, time:float):
        """Update the queue when someone arrive at queue.

        Args:
            id (str): id of the person.
            time (float): Time.

        """
        self.queue.append(id)
        self.history[id] = [time]

    def depart(self, id:str, time:float):
        """Update the queue when someone leave the queue.

        Args:
            id (str): id of the person.
            time (float): Time.
        """
        self.queue.remove(id)
        self.history[id].append(time)
        temp = self.time_in_queue[-1] if self.time_in_queue else 0
        self.time_in_queue.append(temp + (self.history[id][1] - self.history[id][0]))
        # If we want to remove useless data use the folloing line.
        # self.history.pop(id, None)

    def __len__(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)

    def __repr__(self):
        return str(self.queue)
    
class Server:
    """Simulate the server.
    """
    def __init__(self):
        """Paramteters:\n
           1- occupied: If the server is opccupied=True.\n
           2- occupied_time: total time which the server is occupied at.\n
           3- unoccupied_time: total time which the server is not occupied at.\n
           4- history: {id: [time for arriving the server, time for departing the server]}
        """
        self.occupied = False
        self.occupied_time = 0
        self.unoccupied_time = 0
        self.last_time = 0
        self.last_id = None
        self.history = {}

    def occupied_at(self, id:str, time:float):
        """Set the server to occupied.

        Args:
            id (str): id of the person.
            time (float): Time.
        """
        if self.occupied:
            self.history[self.last_id] = [self.last_time, time]
            self.occupied_time += time - self.last_time
        else:
            self.unoccupied_time += (time - self.last_time)
        self.last_time = time
        self.last_id = id
        self.occupied = True

    def unoccupied_at(self, time:float):
        """Set the sever to not occupied.

        Args:
            time (float): Time.
        """
        self.history[self.last_id] = [self.last_time, time]
        self.occupied_time += time - self.last_time
        self.last_time = time
        self.last_id = None
        self.occupied = False

class System:
    """Simulate the system.
    """
    def __init__(self):
        """Parameters:
           1- count_45_min_id = Number of id that have more than 4.5 min time in system.
           2- queue: people in the system.
           3- history: {id: [time when arrive at system, time when departe from system.]}
        """
        self.count_45_min_id = 0
        self.queue = []
        self.history = {}

    def arrive(self, id:str, time:float):
        self.queue.append(id)
        self.history[id] = [time]

    def depart(self, id:str, time:float):
        self.queue.remove(id)
        self.history[id].append(time)
        time = self.history[id][1] - self.history[id][0]
        if time > 4.5:
            self.count_45_min_id += 1
        # If we want to remove useless data use the folloing line.
        # self.history.pop(id, None)
