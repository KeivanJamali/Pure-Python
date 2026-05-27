import hashlib

class Travel_Time_Gen:
    def __init__(self, student_id: str):
        assert isinstance(student_id, str)
        seed_value = int(hashlib.sha3_256(bytes(student_id, "utf-8")).hexdigest(), 16)
        self.param_a = (seed_value%100) / 100.0 + 1.0
        self.param_b = (seed_value%50) / 100.0 + 0.5

    def travel_time(self, capacity: int, flow: int, length: int):
        return self.param_a * length * (1 + self.param_b * (flow/capacity)**4)
    
def travel_time_calculator(capacity, flow, free_flow_travel_time):
    return  free_flow_travel_time * (1 + 0.15 * (flow/capacity)**4)
            
    
    