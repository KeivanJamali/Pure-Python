import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore

class Defind_Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def set_setting(self, nodes_s, nodes_t, edges, log=True):
        self.pos = {}
        self.pos.update(nodes_s)
        self.pos.update(nodes_t)
        self.nodes_s = nodes_s
        self.nodes_t = nodes_t

        for node, value in nodes_s.items():
            self.graph.add_node(node, kind="s", data=None, on=0)

        for node, value in nodes_t.items():
            self.graph.add_node(node, kind="t", data=None, on=0)

        for edge, value in edges.items():
            self.graph.add_edge(edge[0], edge[1], on=value[0])

        self.edge_features = ["on"]
        if log:
            print("Nodes:", self.graph.nodes(data=True))
            print("Edges:", self.graph.edges(data=True))

    def plot_graph(self):
        edge_colors = []
        for u, v, data in self.graph.edges(data=True):
            if data["on"] == 1:
                edge_colors.append("blue")
            else:
                edge_colors.append("black")  # You can change the default color

        # Draw the graph
        nx.draw(self.graph, self.pos, with_labels=True, node_size=1500, font_size=10, 
                node_color="red", edge_color=edge_colors)


class Augmented_Path_Method:
    def __init__(self, problem:Defind_Graph):
        self.problem = problem
        self.graph = problem.graph
        self.s = []
        self.t = []
        for node in problem.graph.nodes(data=True):
            if node[1]["kind"] == "s":
                self.s.append(node[0])
            elif node[1]["kind"] == "t":
                self.t.append(node[0])

    def fit(self):
        for _ in range(4):
            self._step_one_check_empty_in_s()
            self._step_two()
            while True:
                self.path = self._step_three()
                if not self.path:
                    break
                self._step_four()

    def _step_one_check_empty_in_s(self):
        for node in self.s:
            empty = True
            for neighbor in self.graph.neighbors(node):
                if self.graph[node][neighbor]["on"] == 1:
                    self.graph.nodes[node]["data"] = neighbor
                    self.graph.nodes[node]["on"] = 1
                    empty = False
                    break
            if empty:
                self.graph.nodes[node]["data"] = "None"

    def _step_two(self):
        for node in self.t:
            for neighbor in self.graph.neighbors(node):
                if self.graph[node][neighbor]["on"] == 1:
                    self.graph.nodes[node]["on"] = 1
                if self.graph[node][neighbor]["on"] == 0:
                    self.graph.nodes[node]["data"] = neighbor

    def _step_three(self):
        for node in self.s:
            if self.graph.nodes[node]["data"] == "None":
                path = [node]
                # ===================================================
                next_node = self._step_three_move(node=node)
                if not next_node:
                    continue
                path.append(next_node)
                # -----------------------------------------------
                if self.graph.nodes[next_node]["on"] == 0:
                    print(f"[CONG] We found {path}!!!")
                    return path
                else:
                    print(f"[INFO] We found {path} but not good.")
                # ===================================================
                while True:
                    next_node = self._step_three_move(node=next_node)
                    if not next_node:
                        break
                    path.append(next_node)
                    next_node = self._step_three_move(node=next_node)
                    if not next_node:
                        break
                    path.append(next_node)
                    # -----------------------------------------------
                    if self.graph.nodes[path[-1]]["on"] == 0:
                        print(f"[CONG] We found {path}!!!")
                        return path
                    else:
                        print(f"[INFO] We found {path} but not good.")
        return False

    def _step_three_move(self, node):
        for neighbor in self.graph.neighbors(node):
            if self.graph.nodes[neighbor]["data"] == node:
                return neighbor
        return False
        
    def _step_four(self):
        for i in range(len(self.path)-1):
            if self.graph[self.path[i]][self.path[i+1]]["on"] == 0:
                self.graph[self.path[i]][self.path[i+1]]["on"] = 1
                self.graph.nodes[self.path[i]]["on"] = 1
                self.graph.nodes[self.path[i+1]]["on"] = 1

            elif self.graph[self.path[i]][self.path[i+1]]["on"] == 1:
                self.graph[self.path[i]][self.path[i+1]]["on"] = 0

    def plot_graph(self):
        self.tree = Defind_Graph()
        edges = self._rewrite_edges(self.graph.edges(data=True))
        self.tree.set_setting(nodes_s=self.problem.nodes_s, nodes_t=self.problem.nodes_t, edges=edges)
        self.tree.plot_graph()

    def _rewrite_edges(self, edges):
        edges = list(edges)
        edges_output = {}
        for row in edges:
            edges_output[(row[0], row[1])] = [row[2]["on"]]
        return edges_output

