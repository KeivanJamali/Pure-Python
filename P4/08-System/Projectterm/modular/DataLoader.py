import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
from pathlib import Path



class Data_loader:
    def __init__(self, city_name):
        self.city_name = city_name
        self.raw_graph = None
        self.graph = None

    def get_data(self, file_name):
        path_dir = Path(r"D:\All Python\Pure-Python\P4\08-System\Projectterm\data")
        try:
            G = ox.load_graphml(path_dir/(file_name+".graphml"))
            print("[INFO] Data is loaded from the local device.")
        except:
            print("[INFO] Start downloading data...")
            G = ox.graph_from_place(self.city_name, network_type="drive")
            # ox.plot_graph(G)
            ox.save_graphml(G, filepath=path_dir/file_name+".graphml")
            print(f"[INFO] Data is downloaded and stored as {file_name} from the local device.")
        self.raw_graph = G

    def set_setting(self, number_of_nodes):
        self._make_undirected()
        self._extract_largest_connected_components()
        self._customize_component(number_of_nodes=number_of_nodes)
        self._assign_node_label()
        self._assign_edge_label()

    def _make_undirected(self):
        self.raw_graph = self.raw_graph.to_undirected()
        print(f"[INFO] -> Undirected")

    def _extract_largest_connected_components(self):
        components = list(nx.connected_components(self.raw_graph))
        largest_component = max(components, key=len)
        self.graph = self.raw_graph.subgraph(largest_component).copy()
        print(f"[INFO] Largest component founded!")


    def _customize_component(self, number_of_nodes):
        start_node = max(dict(self.graph.degree()).items(), key=lambda x: x[1])[0]
        nodes_seen = set([start_node])
        fringe = set(self.graph[start_node])

        while len(nodes_seen) < number_of_nodes and fringe:
            next_node = max(fringe, key=lambda n: self.graph.degree(n))
            nodes_seen.add(next_node)
            fringe.update(self.graph[next_node])
            fringe -= nodes_seen

        # If fewer than 20 nodes found, warn the user
        if len(nodes_seen) < number_of_nodes:
            print(f"[INFO] Only founded {len(nodes_seen)} connected nodes.")
        else:
            print(f"[INFO] Founded {number_of_nodes} connected nodes.")

        self.graph = self.graph.subgraph(nodes_seen).copy()

        G_standard = nx.Graph()
        G_standard.add_nodes_from(self.graph.nodes(data=True))
        for u, v, data in self.graph.edges(data=True):
            G_standard.add_edge(u, v, **data)
        self.graph = G_standard

    def _assign_node_label(self):
        sorted_nodes = sorted(self.graph.nodes())
        node_label_map = {node_id: i + 1 for i, node_id in enumerate(sorted_nodes)}
        self.graph = nx.relabel_nodes(self.graph, node_label_map, copy=True)
        print("\n[INFO] Node Labels:")
        for original_id, label in node_label_map.items():
            print(f"OSM ID: {original_id}, Label: {label}")

    def _assign_edge_label(self):
        edge_index = {}
        names = []
        for u, v in self.graph.edges():
            label_sum = u + v
            while label_sum in names:
                label_sum += 0.5                    
            names.append(label_sum)
            # Ensure unique key (undirected)
            if (u, v) not in edge_index and (v, u) not in edge_index:
                edge_index[(u, v)] = label_sum
            self.graph.edges[u, v]["ID"] = label_sum
                
        self.edge_index = edge_index
        print("\n[INFO] Edge Indices (based on node label sums):")
        for (u, v), idx in edge_index.items():
            print(f"Edge ({u}, {v}): Index = {idx}")

    def plot_graph(self, graph, original=True, seed=42):
        if original:
            ox.plot_graph(graph)
        else:
            pos = nx.spring_layout(graph, seed=seed)
            nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=800)
            nx.draw_networkx_edge_labels(self.graph, pos,
                edge_labels={edge: idx for edge, idx in self.edge_index.items()})
            plt.title("Subgraph with Edge Indices")
            plt.show()