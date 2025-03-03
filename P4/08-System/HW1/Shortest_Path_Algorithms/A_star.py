import networkx as nx
import heapq
from Shortest_Path_Algorithms import meaturements

class A_Star:
    def __init__(self, graph: nx.Graph, heuristic=None):
        self.graph = graph
        if heuristic:
            self.heuristic = heuristic
        else:
            self.heuristic = self.heuristic_euclidean

    def fit(self, source, target):
        self.source = source
        self.target = target
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
            current_f, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)
            if current_node == self.target:
                print(f"[Successful] Found the path to {self.target}. Early stop!")
                return
            
            for neighbor, weight in self.graph[current_node].items():
                cost = weight["cost"]
                new_distance = self.distances[current_node] + cost

                if new_distance < self.distances[neighbor]:
                    self.distances[neighbor] = new_distance
                    self.predecessors[neighbor] = current_node
                    f_cost = new_distance + self.heuristic(self.graph.nodes[neighbor]["pos"], self.graph.nodes[self.target]["pos"])
                    heapq.heappush(priority_queue, (f_cost, neighbor))
    
    def shortest_path_to(self):
        path = []
        node = self.target
        while node is not None:
            path.append(node)
            node = self.predecessors[node]
        return path[::-1]

    @staticmethod
    def heuristic_euclidean(pos1, pos2):
        """Euclidean distance squared heuristic (faster than sqrt)."""
        x1, y1 = pos1
        x2, y2 = pos2
        return (x2 - x1) ** 2 + (y2 - y1) ** 2


