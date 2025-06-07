import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
from pathlib import Path
import random



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
            name = file_name + ".graphml"
            ox.save_graphml(G, filepath=path_dir/name)
            print(f"[INFO] Data is downloaded and stored as {file_name} from the local device.")
        self.raw_graph = G

    def set_setting(self, number_of_nodes):
        self._make_undirected()
        self._extract_largest_connected_components()
        self._customize_component(number_of_nodes=number_of_nodes, iterations=10)
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


    def _customize_component2(self, number_of_nodes):
        start_node = max(dict(self.graph.degree()).items(), key=lambda x: x[1])[0]
        print(f"[INFO] Start node is {start_node}")

        nodes_seen = set([start_node])
        fringe = set(self.graph[start_node])

        while len(nodes_seen) < number_of_nodes and fringe:
            next_node = max(fringe, key=lambda n: self.graph.degree(n))
            nodes_seen.add(next_node)
            fringe.update(self.graph[next_node])
            self.fringe = fringe
            self.test = next_node
            fringe -= set([next_node])

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

    def _customize_component(self, number_of_nodes, iterations):
        self.graph = nx.Graph(self.graph)
        best_nodes = set()
        best_edges = []
        
        for _ in range(iterations):
            start_node = random.choice(list(self.graph.nodes))
            visited = set([start_node])
            edge_list = []
            queue = [start_node]

            while queue and len(visited) < number_of_nodes:
                current = queue.pop(0)
                neighbors = list(self.graph.neighbors(current))

                for neighbor in neighbors:
                    if len(visited) >= number_of_nodes:
                        break

                    edge = (current, neighbor)
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        edge_list.append(edge)
                    elif edge not in edge_list and (neighbor, current) not in edge_list:
                        edge_list.append(edge)  # Add it if it hasn't already been added in any direction

            if len(visited) == number_of_nodes and len(edge_list) > len(best_edges):
                best_nodes = visited.copy()
                best_edges = edge_list.copy()

        if not best_nodes:
            print("[WARNING] Could not find a connected subgraph with the desired number of nodes.")
            return None

        print(f"[INFO] Found a connected subgraph with {len(best_nodes)} nodes and {len(best_edges)} edges.")
        
        # Build and return the subgraph
        subgraph = self.graph.subgraph(best_nodes).copy()
        self.graph = subgraph
        return subgraph

    def _assign_node_label(self):
        sorted_nodes = sorted(self.graph.nodes())
        node_label_map = {node_id: i + 1 for i, node_id in enumerate(sorted_nodes)}
        self.graph = nx.relabel_nodes(self.graph, node_label_map, copy=True)
        print("\n[INFO] Node Labels:")
        for original_id, label in node_label_map.items():
            print(f"OSM ID: {original_id}, Label: {label}")

    def _assign_edge_label(self):
        edge_index = {}
        names = {}
        for u, v in self.graph.edges():
            label_sum = u + v
            depth = 0
            while label_sum in names.keys():
                depth += 1
                if min([u, v]) < min(names[label_sum]):
                    label_sum -= 0.1/depth
                else:
                    label_sum += 0.1/depth
            names[label_sum] = (u, v)

        values = sorted(list(names.keys()))
        
        counter = 0
        for value in values:
            counter += 1
            u, v = names[value]
            # Ensure unique key (undirected)
            if (u, v) not in edge_index and (v, u) not in edge_index:
                edge_index[(u, v)] = counter
            self.graph.edges[u, v]["ID"] = counter
                
        self.edge_index = edge_index
        print("\n[INFO] Edge Indices (based on node label sums):")
        for (u, v), idx in edge_index.items():
            print(f"Edge ({u}, {v}): Index = {idx}")

    def plot_graph(self, graph, original=True, seed=42):
        if original:
            ox.plot_graph(graph)
        else:
            pos = nx.spring_layout(graph, seed=seed)
            # plt.figure(figsize=(12, 12))
            nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=200)
            nx.draw_networkx_edge_labels(self.graph, pos,
                edge_labels={edge: idx for edge, idx in self.edge_index.items()})
            # Auto adjust plot bounds with padding
            # x_vals, y_vals = zip(*pos.values())
            # plt.xlim(min(x_vals) - 0.001, max(x_vals) + 0.001)
            # plt.ylim(min(y_vals) - 0.001, max(y_vals) + 0.001)

            plt.title("Subgraph with Edge Indices")
            plt.show()