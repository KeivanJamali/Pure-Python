import networkx as nx
import numpy as np
from Shortest_Path_Algorithms import meaturements

class FloydWarshall:
    def __init__(self, graph: nx.Graph):
        self.graph = graph
        self.nodes = list(graph.nodes)
        self.num_nodes = len(self.nodes)
        self.distances = None

    @meaturements.measure_time
    def fit(self):
        # Initialize distance matrix
        self.distances = {u: {v: float("inf") for v in self.nodes} for u in self.nodes}
        for u in self.nodes:
            self.distances[u][u] = 0  # Distance to itself is zero
        
        for u, v, data in self.graph.edges(data=True):
            weight = data.get("cost", float("inf"))
            if self.graph.is_directed():
                self.distances[u][v] = weight
            else:
                self.distances[u][v] = weight
                self.distances[v][u] = weight
        
        # Floyd-Warshall algorithm
        for k in self.nodes:
            for i in self.nodes:
                for j in self.nodes:
                    if self.distances[i][j] > self.distances[i][k] + self.distances[k][j]:
                        self.distances[i][j] = self.distances[i][k] + self.distances[k][j]

    def distance_to(self, source: str, target: str):
        return self.distances[source][target]
