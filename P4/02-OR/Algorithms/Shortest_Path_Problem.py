import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore

class Defind_Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def set_setting(self, nodes, edges):
        self.pos = nodes

        for node, value in nodes.items():
            self.graph.add_node(node)

        for edge, value in edges.items():
            self.graph.add_edge(edge[0], edge[1], cost=value[0])

        self.edge_features = ["cost"]

        print("Nodes:", self.graph.nodes(data=True))
        print("Edges:", self.graph.edges(data=True))

    def plot_graph(self):
        nx.draw(self.graph, self.pos, with_labels=True, node_size=1500, font_size=10, node_color="red")
        features = ""
        for i in self.edge_features:
            features += "{self.graph.edges[edge]['" + i + "']}, "
        template = "f'"+features+"'"
        # print(template)
        edge_labels = {edge: eval(template) for edge in self.graph.edges}
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=edge_labels)

class Dijkestra:
    def __init__(self, problem:Defind_Graph):
        self.problem = problem
        self.graph = self.problem.graph
        self.done = False


    def fit(self, start_node, end_node=None):
        self._step_one_initialize(starter=start_node)
        start = start_node
        self.start_node = start_node
        i = 0
        while start:
            i += 1
            neighbors = self._find_neighbors(node=start)
            # if not neighbors:
            #     break
            for neighbor in neighbors:
                self._step_two_update_info(starter=start, neighbor=neighbor)
            start = self._check_for_new()
            if end_node and start == end_node:
                print(self.extract_solution(node=end_node))
                return f"The solution from {start_node} to {end_node} found sooner!"

        return f"All the path started at {start_node} to other nodes is found now."

    def _step_one_initialize(self, starter: str) -> None:
        nx.set_node_attributes(G=self.graph, values={starter : 0}, name="cost")
        nx.set_node_attributes(G=self.graph, values={starter : None}, name="previous_node")
        nx.set_node_attributes(G=self.graph, values={starter : True}, name="visited")
        for node in self.graph.nodes:
            if not node == starter:
                nx.set_node_attributes(G=self.graph, values={node : float("inf")}, name="cost")
                nx.set_node_attributes(G=self.graph, values={node : None}, name="previous_node")
                nx.set_node_attributes(G=self.graph, values={node : False}, name="visited")

    def _find_neighbors(self, node: str) -> list[str]:
        neighbors = []
        for edge in self.graph.edges:
            if edge[0] == node:
                neighbor = edge[1]
                if not self.graph.nodes[neighbor]["visited"]:
                    neighbors.append(neighbor)
            elif edge[1] == node:
                neighbor = edge[0]
                if not self.graph.nodes[neighbor]["visited"]:
                    neighbors.append(neighbor)
        return neighbors

    def _step_two_update_info(self, starter, neighbor):
        cost_new = self.graph.nodes[starter]["cost"] + self.graph.edges[(starter, neighbor)]["cost"]
        # print(f"[INFO] from {starter} to {neighbor} we calculate the cost of {self.graph.nodes[starter]["cost"]} + {self.graph.edges[(starter, neighbor)]["cost"]} which is compared to {self.graph.nodes[neighbor]["cost"]}...")
        if cost_new < self.graph.nodes[neighbor]["cost"]:
            nx.set_node_attributes(G=self.graph, values={neighbor : starter}, name="previous_node")
            nx.set_node_attributes(G=self.graph, values={neighbor : cost_new}, name="cost")

    def _check_for_new(self) -> str:
        def temp(x):
            result = x[1]["cost"] if not x[1]["visited"] else float(10**10)
            return result
        
        node = min(list(self.graph.nodes(data=True)), key=lambda x: temp(x))
        
        if node[1]["visited"]:
            self.done = True
            # print("[INFO] Nothing found!")
            return False
        
        else:
            self.done = False
            # print(f"[INFO] We found node {node[0]}")
            nx.set_node_attributes(G=self.graph, values={node[0] : True}, name="visited")
            return node[0]

    def extract_solution(self, node):
        how_to_reach = []
        cost = self.graph.nodes[node]["cost"]
        p_node = node
        while p_node != None:
            how_to_reach.append(p_node)
            p_node = self.graph.nodes[p_node]["previous_node"]
        return {"How_to_reahc": list(reversed(how_to_reach)),
                "cost": cost}
