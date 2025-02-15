from pathlib import Path
import pandas as pd

class Tools:
    def __init__(self, travel_info):
        self.path = travel_info
        self.data = pd.read_xml(self.path, xpath="tripinfo")

    def travel_time_calculation(self):
        travel_time = sum(self.data["duration"])
        print(f"Total Travel Time Is : {travel_time}")
        self.total_travel_time = travel_time

base_info = Path("Project_KeivanJamali.tripinfo_base.xml")
advanced_info = Path("Project_KeivanJamali.tripinfo_advanced.xml")

time_base = Tools(travel_info=base_info)
time_advanced = Tools(travel_info=advanced_info)

time_base.travel_time_calculation()
time_advanced.travel_time_calculation()