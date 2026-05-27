import hashlib
import numpy as np

class Demand_Gen:
    def __init__(self, student_id: str):
        assert isinstance(student_id, str)
        self.student_id = student_id
        
    def demand(self, o, d, travel_time=0):
        param = int(hashlib.sha3_256(bytes(self.student_id + str(o) + str(d), "utf-8")).hexdigest(), 16)
        demand = int(param % 100 + 10)
        demand -= travel_time * (demand/100)
        return demand
        
    
