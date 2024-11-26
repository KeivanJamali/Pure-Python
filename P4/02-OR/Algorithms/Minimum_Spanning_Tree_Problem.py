import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore

class Defind_Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def set_setting(self, nodes, edges, log=True):
        self.pos = nodes

        for node, value in nodes.items():
            self.graph.add_node(node)

        for edge, value in edges.items():
            self.graph.add_edge(edge[0], edge[1], cost=value[0])

        self.edge_features = ["cost"]
        if log:
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

class Kruskal:
    def __init__(self, problem:Defind_Graph):
        self.problem = problem
        self.graph = problem.graph
        self.done = False
        self.minimum_tree = []

    def fit(self):
        sorted_edges = self._sort_edges_costs()
        print(sorted_edges)
        self._name_nodes_initially()
        # print(self.graph.nodes(data=True))
        n = len(self.graph.nodes)
        while sorted_edges and len(self.minimum_tree) < n:
            temp = sorted_edges.pop(0)
            if self._check_loop(temp[0], temp[1]):
                continue
            self.minimum_tree.append(temp)
            self._update_nodes_p(temp)
            self._update_nodes_root()
            # print(self.graph.nodes(data=True))
        self.tree = Defind_Graph()
        edges = self._rewrite_edges()
        self.tree.set_setting(nodes=self.problem.pos, edges=edges, log=False)
        self.tree.plot_graph()
        print(self.minimum_tree)
        total_cost = sum(br["cost"] for _, __, br in self.minimum_tree)
        print(f"Total cost in this tree is: {total_cost}")

    def _rewrite_edges(self):
        edges = {}
        for row in self.minimum_tree:
            edges[(row[0], row[1])] = [row[2]["cost"]]
        return edges

    def _sort_edges_costs(self) -> list:
        edges = list(self.graph.edges(data=True))
        sorted_edges = sorted(edges, key=lambda x: x[2]["cost"])
        return sorted_edges
    
    def _name_nodes_initially(self) -> None:
        for node in self.graph.nodes:
            nx.set_node_attributes(G=self.graph, values={node: node}, name="R")
            nx.set_node_attributes(G=self.graph, values={node: 0}, name="P")

    def _update_nodes_p(self, edge) -> None:
        node = max(edge[0], edge[1])
        nx.set_node_attributes(G=self.graph, values={node: min(edge[0], edge[1])}, name="P")
        
    def _update_nodes_root(self) -> None:
        for node in list(self.graph.nodes):
            rest_nodes = [self.graph.nodes[node]["R"]]
            for edge in self.minimum_tree:
                if node in [edge[0], edge[1]]:
                    nx.set_node_attributes(G=self.graph, values={edge[0]: min(self.graph.nodes[edge[1]]["R"], self.graph.nodes[edge[0]]["R"])}, name="R")
                    nx.set_node_attributes(G=self.graph, values={edge[1]: min(self.graph.nodes[edge[1]]["R"], self.graph.nodes[edge[0]]["R"])}, name="R")
            
    def _check_loop(self, a, b) -> bool:
        if self.graph.nodes[a]["R"] == self.graph.nodes[b]["R"]:
            return True
        
        else:
            return False


class Prim:
    def __init__(self, problem:Defind_Graph):
        self.problem = problem
        self.graph = problem.graph
        self.done = False
        self.minimum_tree = []
        self.u = [list(self.graph.nodes)[0]]
        self.s = []
        self.i = self.u[0]
        self.temp_nodes = None
        self.total_cost = 0

    def fit(self):
        self._step_one()
        while True:
            self._step_two_update()
            check = self._step_three()
            if check:
                break

        print(f"Answer found.")
        self.tree = Defind_Graph()
        edges = self._rewrite_edges()
        self.tree.set_setting(nodes=self.problem.pos, edges=edges, log=False)
        self.tree.plot_graph()
        print(f"S list is : {self.s}")
        print(f"U list is : {self.u}")
        print(f"Total cost in this tree is: {self.total_cost}")

    def _step_one(self):
        for node in self.graph.nodes:
            nx.set_node_attributes(G=self.graph, values={node: float("inf")}, name="lamda")
            nx.set_node_attributes(G=self.graph, values={node: None}, name="previous_node")
    
    def _step_two_update(self):
        self.temp_nodes = []
        for edge in self.graph.edges(data=True):
            if edge[0] in self.u and edge[1] not in self.u:
                if edge[2]["cost"] <= self.graph.nodes[edge[1]]["lamda"]:
                    nx.set_node_attributes(G=self.graph, values={edge[1]: edge[2]["cost"]}, name="lamda")
                    nx.set_node_attributes(G=self.graph, values={edge[1]: edge[0]}, name="previous_node")
                    self.temp_nodes.append([edge[1], edge[0], edge[2]["cost"]])
            elif edge[1] in self.u and edge[0] not in self.u:
                if edge[2]["cost"] <= self.graph.nodes[edge[1]]["lamda"]:
                    nx.set_node_attributes(G=self.graph, values={edge[0]: edge[2]["cost"]}, name="lamda")
                    nx.set_node_attributes(G=self.graph, values={edge[0]: edge[1]}, name="previous_node")
                    self.temp_nodes.append([edge[0], edge[1], edge[2]["cost"]])

    def _step_three(self):
        if self.temp_nodes:
            # print("choices are", self.temp_nodes)
            temp = min(self.temp_nodes, key=lambda x: x[2])
            # print("minimum is ", temp)
        else:
            return True
        self.u.append(temp[0])
        self.s.append((temp[1], temp[0]))
        self.total_cost += temp[2]

        if list(self.graph.nodes) == self.u:
            return True
        else:
            return False

    def _rewrite_edges(self):
        edges = {}
        for row in self.s:
            edges[(row[0], row[1])] = [self.graph.edges[(row[0], row[1])]["cost"]]
        return edges