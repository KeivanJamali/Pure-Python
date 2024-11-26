import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore


class Defind_Graph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.pos = None
        self.edge_features = None

    def set_setting(self, nodes, edges, log=True):
        self.pos = nodes

        for node, value in nodes.items():
            self.graph.add_node(node)

        for edge, value in edges.items():
            self.graph.add_edge(edge[0], edge[1], max_flow=value[0], current_flow=value[1])

        self.edge_features = ["max_flow", "current_flow"]
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


class Ford_Furkerson:
    def __init__(self, problem:Defind_Graph):
        self.problem = problem
        self.graph = problem.graph


    def fit(self, start, end):
        self.source = start
        self.sink = end
        self._ford_fulkerson_algorithm()

    def _bfs(self):
        self.parent = {}
        visited = {node: False for node in self.graph.nodes()}
        queue = [self.source]
        # print(queue)
        # raise
        visited[self.source] = True

        while queue:
            u = queue.pop(0)

            for node in self.graph.neighbors(u):
                # Check for residual capacity (max_flow - current_flow > 0)
                if not visited[node] and self.graph[u][node]['max_flow'] > self.graph[u][node]['current_flow']:
                    queue.append(node)
                    visited[node] = True
                    self.parent[node] = (u, "+")
                    if node == self.sink:
                        return True

            for node in self.graph.predecessors(u):
                if not visited[node] and self.graph[node][u]['current_flow'] > 0:
                    queue.append(node)
                    visited[node] = True
                    self.parent[node] = (u, '-')  # Store with "-" for backward edge
                    if node == self.sink:  # Stop if we reached the sink
                        return True
        return False
    
    def _correction(self, path, start):
        for i, (node, previous_node) in enumerate(path.items()):
            if start == previous_node[0]:
                new_path = path.copy()
                new_path.pop(node)
                if node == self.sink:
                    print(", " + node + "/" + previous_node[1])
                    return ", " + node + "/" + previous_node[1]
                else:
                    # print(", " + node + "/" + previous_node[1])
                    print(node)
                    return ", " + node + "/" + previous_node[1] + self._correction(new_path, node)
        return 
    def _correction(self, path):
        result = []
        pp = self.sink
        previous_node = [False, False]
        while previous_node[0] != self.source:
            for i, (node, previous_node) in enumerate(path.items()):
                if node == pp:
                    result.append([node, previous_node[1]])
                    pp = previous_node[0]
                    break
        result.append([self.source, "+"])
        return list(reversed(result))

                
    def _correction2(self, path):
        new_path = []
        for i in range(len(path)-1):
            member = [path[i][0], path[i+1][1]]
            new_path.append(member)
        new_path.append([self.sink, "None"])
        return new_path


    def _calculation_to_find_flow(self, path):
        delta = float("inf")
        for i in range(len(path) - 1):
            if path[i][1] == "+":
                delta = min(delta, self.graph[path[i][0]][path[i+1][0]]["max_flow"] - self.graph[path[i][0]][path[i+1][0]]["current_flow"])
            elif path[i][1] == "-":
                delta = min(delta, self.graph[path[i+1][0]][path[i][0]]["current_flow"])
        return delta

    def current_max_flow(self):
        flow = 0
        for node in self.graph.neighbors(self.source):
            flow += self.graph[self.source][node]["current_flow"]
        return flow

    def _ford_fulkerson_algorithm(self):
        max_flow = self.current_max_flow()
        while True:
            check = self._bfs()
            if not check:
                break            
            path = self._correction2(self._correction(self.parent))
            self.path = path
            delta = self._calculation_to_find_flow(path)
            max_flow += delta

            for i in range(len(path) - 1):
                if path[i][1] == "+":
                    self.graph[path[i][0]][path[i+1][0]]["current_flow"] += delta
                elif path[i][1] == "-":
                    self.graph[path[i+1][0]][path[i][0]]["current_flow"] -= delta

            print(self.graph.edges(data=True))
            
        self._plot_graph()
        print(f"Max Flow: {max_flow}")  # Output the maximum flow
    
    def _rewrite_edges(self, edges):
        edges = list(edges)
        edges_output = {}
        for row in edges:
            edges_output[(row[0], row[1])] = [row[2]["max_flow"], row[2]["current_flow"]]
        return edges_output


    def _plot_graph(self):
        self.tree = Defind_Graph()
        edges = self._rewrite_edges(self.graph.edges(data=True))
        self.tree.set_setting(nodes=self.problem.pos, edges=edges, log=False)
        self.tree.plot_graph()