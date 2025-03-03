import networkx as nx

class Graph:
    def __init__(self, directed:bool=False):
        if directed:
            self.graph = nx.DiGraph()
        else:
            self.graph = nx.Graph()

    def set_setting(self, nodes:dict, edges:dict, ):
        for node, value in nodes.items():
            self.graph.add_node(node, **value)

        for edge, value in edges.items():
            self.graph.add_edge(edge[0], edge[1], **value)

        self.edge_attributes = set()
        self.node_attributes = set()

        for _, attr in self.graph.nodes(data=True):
            self.node_attributes.update(attr.keys())
        for _, _, attr in self.graph.edges(data=True):
            self.edge_attributes.update(attr.keys())

    def plot_graph(self, node_label:bool, edge_label:bool):
        pos = nx.get_node_attributes(self.graph, name="pos")
        nx.draw(self.graph, pos, with_labels=True, node_size=1500, font_size=10, node_color="red")

        # edge label with weights
        if edge_label:
            features = ""
            for i in self.edge_attributes:
                features += "{self.graph.edges[edge]['" + i + "']}, "
            template = "f'"+features[:-2]+"'"
            # print(template)
            edge_labels = {edge: eval(template) for edge in self.graph.edges}
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)

        # node label with weights
        if node_label:
            features = ""
            for i in self.node_attributes:
                features += "{self.graph.nodes[node]['" + i + "']}, "
            template = "f'"+features[:-2]+"'"
            # print(template)
            node_labels = {node: eval(template) for node in self.graph.nodes}
            pos_with_offset = {node: (x+0.4, y) for node, (x, y) in pos.items()}
            nx.draw_networkx_labels(self.graph, pos_with_offset, labels=node_labels, verticalalignment="bottom")