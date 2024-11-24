import pandas as pd

trip_info_path = r"D:\All Python\Pure-Python\P4\03-Advanced transportation\SUMO\P1\OUTPUT.xml"
edge_info_path = r"D:\All Python\Pure-Python\P4\03-Advanced transportation\SUMO\P1\EDGEDATA.xml"

trip_data = pd.read_xml(trip_info_path, xpath="tripinfo")
trip_travel_time = sum(trip_data["duration"])

edge_data = pd.read_xml(edge_info_path, xpath="interval/edge")
edge_data["traveltime_output"] = edge_data.apply(lambda row: row["traveltime"] * max(row["entered"], row["left"]), axis=1)
edge_travel_time = sum(edge_data["traveltime_output"])
print("Travel time according to each trip in the Trip-Info file is ", trip_travel_time)
print("Travel time according to links in the Edge_Info file is ", edge_travel_time)

