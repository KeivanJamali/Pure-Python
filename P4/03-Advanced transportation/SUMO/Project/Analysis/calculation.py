import pandas as pd

class Tools:
    def __init__(self, travel_info):
        self.path = travel_info
        self.data = pd.read_xml(self.path, xpath="tripinfo")

    def travel_time_calculation(self):
        travel_time = sum(self.data["duration"])
        print(f"Total Travel Time Is : {travel_time}")
        self.total_travel_time = travel_time
