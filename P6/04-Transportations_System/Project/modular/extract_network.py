import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path

default_network_xy = Path("/Users/keivanjamali/Projects/Pure-Python/P6/04-Transportations_System/Project/data/SiouxFallsXY.csv")
default_network = Path("/Users/keivanjamali/Projects/Pure-Python/P6/04-Transportations_System/Project/data/SiouxFallsNetwork.csv")

class Graph:
    def __init__(self, xy_file_path: str = None, network_file_path: str = None):
        xy_path = default_network_xy if not xy_file_path else xy_file_path
        netwrok_path = default_network if not network_file_path else network_file_path
        data_network = pd.read_csv(netwrok_path)
        data_xy_pos = pd.read_csv(xy_path, index_col=0)
        data_xy_pos = data_xy_pos.set_index('node').apply(lambda row: (row.x, row.y), axis=1).to_dict()
        graph = nx.from_pandas_edgelist(data_network, source="from", target="to", edge_attr=True, create_using=nx.DiGraph())
        nx.set_node_attributes(graph, data_xy_pos, 'pos')
        self.graph: nx.DiGraph = graph
        self.enable_seed = False
                
    def plot(self, attr: str = None):
        plt.figure(figsize=(12, 12))
        nx.draw(self.graph, with_labels=True, pos=nx.get_node_attributes(self.graph, "pos"),
                arrows=True)
        if attr:
            attributes = nx.get_edge_attributes(self.graph, attr)
            attributes_revised = dict()
            for k, v in attributes.items():
                o, d = k
                o_x, o_y = self.graph.nodes[o]["pos"]
                d_x, d_y = self.graph.nodes[d]["pos"]
                if o_x <= d_x and o_y >= d_y: # put the first to left
                    v2 = attributes[(k[1], k[0])]
                    attributes_revised[(min(k), max(k))] = f"{int(round(v))} | {int(round(v2))}"                    
                elif o_x >= d_x: # put the first right
                    v2 = attributes[(k[1], k[0])]
                    attributes_revised[(min(k), max(k))] = f"{int(round(v2))} | {int(round(v))}" 
            nx.draw_networkx_edge_labels(self.graph,
                                        pos=nx.get_node_attributes(self.graph, "pos"),
                                        edge_labels=attributes_revised,
                                        font_size=9, font_color="C5")
        plt.title("Sioux Falls Network")
        plt.show()

    def add_free_flow_speed(self, seed: int): # add travel time in min
        if not self.enable_seed:
            np.random.seed(seed)
            self.enable_seed = True
            
        for u, v, data in self.graph.edges(data=True):
            data["free_flow_speed"] = np.random.uniform(40, 100)
            data["free_flow_travel_time"] = (data["length"]/1000) / data["free_flow_speed"] * 60

    def add_capacity(self, seed: int):
        if not self.enable_seed:
            np.random.seed(seed)
            self.enable_seed = True
            
        for u, v, data in self.graph.edges(data=True):
            data["capacity"] = np.random.uniform(1000, 4000)
            
    def add_OD_demand(self, seed: int):
        if not self.enable_seed:
            np.random.seed(seed)
            self.enable_seed = True
            
        for o in self.graph.nodes():
            for d in self.graph.nodes():
                if o != d:
                    if np.random.rand() < 0.3: # 30% chance of having demand
                        demand = int(np.random.uniform(100, 1000))
                    else:
                        demand = 0
                    self.graph.nodes[o].setdefault("OD_demand", dict())[d] = demand

    def add_percent_to_OD(self, percent: float):
        for o in self.graph.nodes():
            for d in self.graph.nodes():
                if o != d:
                    demand = self.graph.nodes[o].setdefault("OD_demand", dict()).get(d, 0)
                    self.graph.nodes[o]["OD_demand"][d] = demand * (1 + percent)

    def reduce_capacity_by_percent(self, percent: float):
        for u, v, data in self.graph.edges(data=True):
            data["capacity"] = data["capacity"] * (1 - percent)
    
    def add_zero_flow(self):
        for u, v in self.graph.edges():
            self.graph[u][v]["flow"] = 0
            self.graph[u][v]["previous_flow"] = 0
            self.graph[u][v]["y"] = 0
            
    def get_top_crowded_edges(self, top_n: int = 5):
        edge_flows = [(u, v, data["flow"]) for u, v, data in self.graph.edges(data=True)]
        edge_flows.sort(key=lambda x: x[2], reverse=True)
        return edge_flows[:top_n]
    
    def get_top_long_travel_time_edges(self, top_n: int = 5):
        edge_travel_times = [(u, v, data["free_flow_travel_time"]) for u, v, data in self.graph.edges(data=True)]
        edge_travel_times.sort(key=lambda x: x[2], reverse=True)
        return edge_travel_times[:top_n]