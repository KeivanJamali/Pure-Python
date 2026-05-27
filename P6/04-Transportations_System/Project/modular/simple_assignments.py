import pandas as pd
import networkx as nx
from math import sqrt
from pathlib import Path
from modular.travel_time_generator import Travel_Time_Gen
from modular.demand_generator import Demand_Gen
from modular.extract_network import Graph

class engine:
    def __init__(self, graph: Graph, student_id: str, init_flow=0, init_capacity=1000):
        self.student_id = student_id
        self.network: Graph = graph
        self.t_gen = Travel_Time_Gen(student_id)
        self.d_gen = Demand_Gen(student_id)
        self.od = pd.DataFrame(0, columns=sorted(list(self.network.graph.nodes)), 
                               index=sorted(list(self.network.graph.nodes)))
        for u, v in self.network.graph.edges:
            self.network.graph[u][v]["flow"] = init_flow
            self.network.graph[u][v]["capacity"] = init_capacity
    
    def update_travel_times(self):
        for u, v in self.network.graph.edges:
            l = float(self.network.graph[u][v]["length"]) / 1000
            flow = self.network.graph[u][v]["flow"]
            capacity = self.network.graph[u][v]["capacity"]
            self.network.graph[u][v]["travel_time"] = self.t_gen.travel_time(capacity=capacity, flow=flow, length=float(l))
        
    def update_demand(self):
        for i in self.od.index:
            for j in self.od.columns:
                self.od.loc[i, j] = self.d_gen.demand(i, j) if i!=j else 0
        
    def shortest_path_single_to_all(self, o):
        paths = nx.single_source_all_shortest_paths(self.network.graph,
                                                    o, weight="travel_time")
        if paths:
            return dict(paths)
        else:
            None
    
    def assign_by_origin(self, o, percentage: float):
        paths = self.shortest_path_single_to_all(o)
        if paths:
            for j in self.od.columns:
                if j != o:
                    if j in paths.keys():
                        demand = self.od.loc[o, j] * percentage
                        selected_path = min(paths[j])
                        for z in range(len(selected_path)-1):
                            self.network.graph[selected_path[z]][selected_path[z+1]]["flow"] = self.network.graph[selected_path[z]][selected_path[z+1]]["flow"] + float(demand)
                
    def run_allornothing(self):
        self.update_travel_times()
        self.update_demand()
        for o in sorted(self.network.graph.nodes()):
            self.assign_by_origin(o=o, percentage=1)
        print(f"[INFO] Success All Or Nothing Assignment!!!")
            
    def run_incremental_fixed(self, fixed_n):
        percentage = 1 / fixed_n
        for i in range(fixed_n):
            self.update_demand()
            self.update_travel_times()
            for o in self.network.graph.nodes():
                self.assign_by_origin(o=o, percentage=percentage)
        print(f"[INFO] Success Incremental Assignment after {fixed_n} steps!!!")
        
    def run_incremental_fixed_with_percentage(self, fixed_n, percentage):
        total_perc = 0
        for i in range(fixed_n):
            self.update_demand()
            self.update_travel_times()
            temp = percentage * (1 - percentage) ** i
            total_perc += temp
            for o in self.network.graph.nodes():
                self.assign_by_origin(o=o, percentage=temp)
        print(f"[INFO] Success Incremental Assignment after {fixed_n} steps total assign of={total_perc}% !!!")
        
    def run_incremental_percentage(self, percentage, threshold=1e-8):
        total_perc = 0
        step = 0
        while True:
            self.update_demand()
            self.update_travel_times()
            temp = percentage * (1 - percentage) ** step
            if temp < threshold:
                break
            total_perc += temp
            for o in self.network.graph.nodes():
                self.assign_by_origin(o=o, percentage=temp)
            step += 1
        print(f"[INFO] Success Incremental Assignment after {step} steps total assign of={total_perc}% !!!")

    def get_important_number(self):
        s = 0
        for u, v in self.network.graph.edges:
            flow = self.network.graph[u][v]["flow"]
            s += hash((u, v, float(flow)))%10000
        return s

    def get_result_as_file(self, file_name:str):
        file_path = Path(file_name)
        with open(file_path, "w") as f:
            for u, v in self.network.graph.edges:
                flow = self.network.graph[u][v]["flow"]
                f.write(f"{u}, {v}, {flow}\n")
        print(f"[INFO] File {file_name} created successfully.")

    def get_total_flow(self):
        s = 0
        for u,v in self.network.graph.edges:
            flow = self.network.graph[u][v]["flow"]
            s += flow
        return s
        
    ####################################################################################################

    def run_incremental_wrong_method(self, percentage, threshold=1e-8, steps=10):
        huge_data = {}
        for o in self.network.graph.nodes():
            paths = self.shortest_path_single_to_all(o)
            huge_data[o] = {}
            for k, values in paths.items():
                if k == o:
                    continue
                huge_data[o][k] = {}
                
        step = 0
        while True:
            self.update_demand()
            self.update_travel_times()
            for o in self.network.graph.nodes():
                paths = self.shortest_path_single_to_all(o)
                if paths:
                    for j in self.od.columns:
                        if j != o:
                            if j in paths.keys():
                                demand = round(self.od.loc[o, j], 2)
                                selected_path = tuple(min(paths[j]))
                                if selected_path not in huge_data[o][j].keys():
                                    huge_data[o][j][selected_path] = 0
                                for path, flow in huge_data[o][j].items():
                                    if path == selected_path:
                                        huge_data[o][j][path] += percentage * (demand - flow)
                                        for z in range(len(path)-1):
                                            self.network.graph[list(path)[z]][list(path)[z+1]]["flow"] += percentage * (demand - flow)   
                                    else:
                                        huge_data[o][j][path] -= percentage * flow
                                        for z in range(len(path)-1):
                                            self.network.graph[list(path)[z]][list(path)[z+1]]["flow"] -= percentage * flow
            step += 1
            if step > steps:
                print("Reach to end")
                break
        
