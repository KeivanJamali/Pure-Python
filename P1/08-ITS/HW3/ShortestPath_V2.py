import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from tqdm.auto import tqdm


class ShortestPath:
    def __init__(self) -> None:
        self.graph_ = None
        self.graph_list = None
        self.start = None
        self.target = None
        self.shortest = None
        self.path = None
        self.shortest_path = None
        self.results = None

    @staticmethod
    def _heuristic(node, target):
        """
        Calculate the Euclidean distance between two nodes as the heuristic.

        Parameters:
        - node: The current node.
        - target: The target node.

        Returns:
        - The Euclidean distance between the current node and the target node.
        """
        return np.linalg.norm(target - node)

    def _update_path(self, path: np.ndarray, v) -> None:
        for i in range(len(path) - 1):
            self.graph_[path[i]][path[i + 1]] = self.graph_[path[i]][path[i + 1]] * (1 + 0.3 * (v / 4000) ** 2)

    def fit(self, graph_: dict, start: int, target: int) -> tuple:
        """
        Fits the given graph with the A* algorithm to find the shortest path from a start node to a target node.

        Parameters:
            graph_ (dict): A dictionary representing the graph.
            start (int): The start node.
            target (int): The target node.

        Returns:
            tuple: A tuple containing the shortest path from the start node to the target node,
                   and the path taken to reach the target node.
        """
        self.graph_ = graph_
        self.graph_list = list(graph_)
        self.start = start
        self.target = target
        self.shortest, self.path = self._astar_method()
        print("Done Shortest path")
        self.shortest_path = self.shortest[target]
        # self.graph_plotting(self.path)
        self.results = pd.DataFrame({self.shortest_path: self.path})
        return self.shortest_path, self.path

    def fit_flow(self, graph_: dict, start: int, target: int, flow: int, step: int) -> None:
        """
        Fits the given graph with the A* algorithm to find the shortest path from a start node to a target node.

        Parameters:
            graph_ (dict): A dictionary representing the graph.
            pos (dict): A dictionary representing the position of each node.
            start (int): The start node.
            target (int): The target node.
            flow (int): Total number of vehicles.
            step (int): After how many vehicles we should update our travel time.

        Returns:
            tuple: A tuple containing the shortest path from the start node to the target node,
                   and the path taken to reach the target node.
        """
        self.graph_ = graph_
        self.graph_list = list(graph_)
        self.start = start
        self.target = target
        for _ in tqdm(range(0, flow, step)):
            self.shortest, self.path = self._astar_method()
            self.shortest_path = self.shortest[target]
            # self.graph_plotting(self.path, name=f"Question3_step{i}")
            self._update_path(path=self.path, v=step)
            if self.results is None:
                self.results = pd.DataFrame({self.shortest_path: self.path})
            else:
                new = pd.DataFrame({self.shortest_path: self.path})
                self.results = pd.concat([self.results, new], axis=1)
            # print(self.shortest_path, self.path)
        self.save_results("result-whole-run")

    def _astar_method(self) -> tuple:
        """
        A* algorithm implementation.

        This private method performs the A* algorithm to find the shortest path between
        the start node and the target node in a graph. It returns the distances from the
        start node to each node in the graph and the shortest path as a tuple.

        Returns:
            distances_ (numpy.ndarray): An array of distances from the start node to each node in the graph.
            shortest_path (list): A list representing the shortest path from the start node to the target node.
        """
        num_nodes = len(self.graph_list)
        visited = np.zeros(num_nodes, dtype=bool)
        distances_ = np.full(num_nodes, np.inf)
        index_start = self.graph_list.index(self.start)
        distances_[index_start] = 0
        parents = np.full(num_nodes, -1, dtype=int)
        pbar = tqdm(total=12275)
        while True:
            pbar.update(1)
            current_node = None
            current_distance = np.inf
            # using heuristic
            for index in range(num_nodes):
                node = self.graph_list[index]
                # print(visited)
                if not visited[index] and distances_[index] + self._heuristic(node, self.target) < current_distance:
                    current_node = node
                    current_distance = distances_[index] + self._heuristic(node, self.target)
                    current_index = index

            if current_node is None:
                break

            visited[current_index] = True
            # update costs of each node
            for neighbor, weight in self.graph_[current_node].items():
                try:
                    distance = distances_[current_index] + weight
                    index_neighbor = self.graph_list.index(neighbor)
                    if distance < distances_[index_neighbor]:
                        distances_[index_neighbor] = distance
                        parents[index_neighbor] = current_node
                except:
                    pass
        pbar.close()
        # print("Done Part 1")
        shortest_path = self._reconstruct_path(parents)
        # print("Done Part 2")
        return distances_, list(map(int, shortest_path))

    def _reconstruct_path(self, parents: np.ndarray):
        """
        Reconstructs the path from the target node to the start node.

        Parameters:
            parents (dict): A dictionary mapping each node to its parent node.

        Returns:
            list: The path from the target node to the start node.
        """

        index_current_node = self.graph_list.index(self.target)
        current_node = self.target
        path = [current_node]

        while current_node != self.start:
            try:
                current_node = parents[index_current_node]
                index_current_node = self.graph_list.index(current_node)
                path.append(current_node)
            except:
                print("There is no way to catch it!!!")
                break

        path.reverse()
        return path

    def graph_plotting(self, given_path: np.ndarray, name: str = "Question3_tree.svg"):
        """
        Generates a plot of the given networkx graph with a highlighted path.

        Args:
            given_path (list): A list of nodes representing the path to highlight.
            pos (dict): A dictionary representing the position of each node.
            name (str): The name of saved plot.

        Returns:
            None
        """
        # Create a networkx graph from the adjacency dictionary
        g = nx.DiGraph(self.graph_)
        pos = nx.spring_layout(g, seed=42)
        nx.draw_networkx_nodes(g, pos)
        nx.draw_networkx_edges(g, pos)
        nx.draw_networkx_labels(g, pos)
        path = given_path
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(g, pos, edgelist=path_edges, edge_color='r', width=2)
        # plt.savefig(f"plots/{name}.svg", format="svg")
        plt.show()
        # plt.close()

    def save_results(self, name: str = "result"):
        self.results.to_csv(f"results/{name}.csv")
