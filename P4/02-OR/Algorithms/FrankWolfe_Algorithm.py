import networkx as nx
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd
from colorama import Fore

class Defind_Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def set_setting(self, nodes, edges, origin, destination):
        self.pos = nodes
        self.origin = origin
        self.destination = destination

        for node, value in nodes.items():
            if node in origin.keys():
                self.graph.add_node(node, production=origin[node], attraction=False)
            elif node in destination.keys():
                self.graph.add_node(node, attraction=destination[node], production=False)
            else:
                self.graph.add_node(node, attraction=False, production=False)

        for edge, value in edges.items():
            self.graph.add_edge(edge[0], edge[1], cost=value[0], formula=value[1])

        self.edge_features = ["cost", "formula"]
        self.data_cost = pd.DataFrame(columns=["path", "cost"])
        for o in origin:
            for d in destination:
                data = self._find_path_with_costs(o, d)
                self.data_cost = pd.concat([self.data_cost, data], ignore_index=True)

    def _find_path_with_costs(self, source, target):
        all_paths = list(nx.all_simple_paths(self.graph, source=source, target=target))
        costs = []
        for path in all_paths:
            cost = []
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                cost.append(self.graph[u][v]['cost'])
            costs.append(cost)

        data = pd.DataFrame({"path": all_paths, "cost": costs})
        return data

    def plot_graph(self):
        nx.draw(self.graph, self.pos, with_labels=True, node_size=1500, font_size=10, node_color="red")
        features = ""
        for i in self.edge_features:
            features += "{self.graph.edges[edge]['" + i + "']}, "
        template = "f'"+features+"'"
        # print(template)
        edge_labels = {edge: eval(template) for edge in self.graph.edges}
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=edge_labels)


class Frank_Wolf:
    def __init__(self, problem):
        self.problem = problem
        self.origin = problem.origin
        self.destination = problem.destination
        self.graph = problem.graph

        params_t_str = ["t_"+self.graph.edges[edge]["cost"] for edge in self.graph.edges]
        params_x_str = ["x_"+self.graph.edges[edge]["cost"] for edge in self.graph.edges]
        
        self.params_t = sp.symbols(params_t_str)
        self.params_x = sp.symbols(params_x_str)
        expr = [sp.sympify(self.graph.edges[edge]["formula"]) for edge in self.graph.edges]
        self.expressions = pd.DataFrame({"cost_function": params_t_str,
                                         "parameter": params_x_str,
                                         "function": expr})
        
        expr = []
        self.test = []
        for i in self.problem.data_cost.index:
            temp = 0
            for ex in self.problem.data_cost.iloc[i, 1]:
                ex_a = "t_"+ex
                ex_b = list(self.expressions[self.expressions["cost_function"] == ex_a]["function"])[0]
                temp += ex_b
            expr.append(temp)

        self.path_expressions = self.problem.data_cost.copy()
        self.path_expressions["function"] = expr
        
        self.columns = [self.expressions.iloc[i, 0] for i in self.expressions.index]
        self.columns.append("None")
        self.data = None

    def fit(self):
        self._initialization()

    def _initialization(self):
        t = [[]]
        for row in self.path_expressions.index:
            temp = self.path_expressions.iloc[row, 2]
            for x in self.params_x:
                temp = temp.subs(x, 0)
            t[0].append(temp)
        t[0].append("None")
        self.data = pd.DataFrame(t, columns=self.columns)
        x = self._find_x()
        # self.data.loc[len(self.data)] = x

        
    def _find_x(self) -> list:
        for o in self.origin.keys():
            for d in self.destination.keys():
                self._find_min_cost(o, d)
                print("HHHELLLL")

    def _find_min_cost(self, o, d):
        for row in self.path_expressions.index:
            path = self.path_expressions.iloc[row, 0]
            if path[0] == o and path[-1] == d:
                