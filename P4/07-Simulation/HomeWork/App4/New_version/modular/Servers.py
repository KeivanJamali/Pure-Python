import simpy

class FCFSStation:
    def __init__(self, env:simpy.Environment, capacity):
        self.env = env
        self.resource = simpy.Resource(capacity=capacity)
        self.stats = []

    def serve(self, visit, customer):
        with self.resource.request() as request:
            yield request
            visit.start_time = self.env.now
            yield self.env.timeout(visit.service_time)
            visit.end_time = self.env.now
            self.stats.append(visit.end_time - visit.start_time)