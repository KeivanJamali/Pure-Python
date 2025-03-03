import networkx as nx
from Shortest_Path_Algorithms import meaturements

class Bellman_Ford:
    def __init__(self, graph:nx.Graph):
        self.graph = graph

    def fit(self, source:str, target:str=None):
        self.source = source
        self.target = target
        self._algorithm()

    @meaturements.measure_time
    def _algorithm(self):
        # Step 1: Initialize distances
        self.distances = {node: float('inf') for node in self.graph}
        self.distances[self.source] = 0

        # Step 2: Relax edges |V| - 1 times
        for _ in range(len(self.graph.nodes) - 1):
            for u in self.graph:
                for v, weight in self.graph[u].items():
                    if self.distances[u] != float('inf') and self.distances[u] + weight["cost"] < self.distances[v]:
                        self.distances[v] = self.distances[u] + weight["cost"]

        # Step 3: Check for negative weight cycles
        for u in self.graph:
            for v, weight in self.graph[u].items():
                if self.distances[u] != float('inf') and self.distances[u] + weight["cost"] < self.distances[v]:
                    raise ValueError("Graph contains negative weight cycle")
