import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore


class Defind_Graph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.pos = None
        self.edge_features = None

    def set_setting(self, nodes, edges):
        self.pos = nodes

        for node, value in nodes.items():
            self.graph.add_node(node)

        for edge, value in edges.items():
            self.graph.add_edge(edge[0], edge[1], max_flow=value[0], current_flow=value[1])

        self.edge_features = ["max_flow", "current_flow"]

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

    def ford_furkerson(self, starter):
        # step one
        max_flow = 0
        for edge, value in nx.get_edge_attributes(self.graph, "current_flow").items():
            if edge[0] == starter:
                max_flow += value
        print(Fore.RESET + "[INFO] Step One: Maximum flow is : " + Fore.LIGHTGREEN_EX + f"{max_flow}" + Fore.RESET + " .")

        # Step two