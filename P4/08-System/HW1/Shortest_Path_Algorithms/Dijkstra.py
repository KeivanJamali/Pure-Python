import networkx as nx
import heapq
from Shortest_Path_Algorithms import meaturements

class Dijkstra:
    def __init__(self, graph:nx.Graph):
        self.graph = graph

    def fit(self, source:str, target:str=None, early_stop:bool=True):
        self.source = source
        self.target = target
        self.early_stop = early_stop
        self._algorithm()

    @meaturements.measure_time
    def _algorithm(self):
        self.distances = {node: float("inf") for node in self.graph}
        self.distances[self.source] = 0
        self.predecessors = {node: None for node in self.graph}

        priority_queue = [(0, self.source)]
        heapq.heapify(priority_queue)

        visited = set()

        while priority_queue:
            if self.target in visited and  self.early_stop:
                print(f"[Successful] Find the path to node {self.target} sooner. Early stop!")
                return

            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node in visited:
                continue

            visited.add(current_node)
            # print(f"[INFO] We add node {current_node} as visited.")
            for neighbor, weight in self.graph[current_node].items():
                new_distance = current_distance + weight["cost"]
                if new_distance < self.distances[neighbor]:
                    self.distances[neighbor] = new_distance
                    self.predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))


    def distance_to(self, target:str):
        return self.distances[target]
    
    def shortest_path_to(self, target):
        path = []
        node = target
        while node is not None:
            path.append(node)
            node = self.predecessors[node]
        return path[::-1]