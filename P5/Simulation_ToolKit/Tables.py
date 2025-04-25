from scipy import stats

class Stats:
    def __init__(self):
        self.last_t_value = None
        self.last_z_value = None

    def t_value_for_percentage(self, point, freedom_degree):
        self.last_t_value = stats.t.ppf(point, freedom_degree)
        return self.last_t_value
    
    def t_value_for_
    
    def z_value(self, point):
        self.last_z_value = stats.norm.ppf(point)
        return self.last_z_value