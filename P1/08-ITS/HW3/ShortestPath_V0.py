import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class ShortestPath:
    def __init__(self) -> None:
        self.graph_ = None
        self.start = None
        self.target = None
        self.shortest = None
        self.path = None
        self.shortest_path = None

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
        self.start = start
        self.target = target
        self.shortest, self.path = self._astar_method()
        self.shortest_path = self.shortest[target]
        return self.shortest_path, self.path

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
        num_nodes = len(self.graph_)
        visited = np.zeros(num_nodes, dtype=bool)
        # print(visited)
        distances_ = np.full(num_nodes, np.inf)
        distances_[self.start] = 0
        parents = np.full(num_nodes, -1, dtype=int)

        while True:
            current_node = None
            current_distance = np.inf
            # using heuristic
            for node in range(num_nodes):
                if not visited[node] and distances_[node] + self._heuristic(node, self.target) < current_distance:
                    current_node = node
                    current_distance = distances_[node] + self._heuristic(node, self.target)

            if current_node is None:
                break

            visited[current_node] = True
            # update costs of each node
            for neighbor, weight in self.graph_[current_node].items():
                distance = distances_[current_node] + weight
                if distance < distances_[neighbor]:
                    distances_[neighbor] = distance
                    parents[neighbor] = current_node
        shortest_path = self._reconstruct_path(parents)

        return distances_, shortest_path

    def _reconstruct_path(self, parents: np.ndarray):
        """
        Reconstructs the path from the target node to the start node.

        Parameters:
            parents (dict): A dictionary mapping each node to its parent node.

        Returns:
            list: The path from the target node to the start node.
        """
        current_node = self.target
        path = [current_node]

        while current_node != self.start:
            current_node = parents[current_node]
            path.append(current_node)

        path.reverse()
        return path

    def graph_plotting(self, given_path: np.ndarray, pos: dict, name: str = "Question1_tree"):
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
        nx.draw_networkx_nodes(g, pos)
        nx.draw_networkx_edges(g, pos)
        nx.draw_networkx_labels(g, pos)
        path = given_path
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(g, pos, edgelist=path_edges, edge_color='r', width=2)
        plt.savefig(f"plots/{name}.svg", format="svg")
        plt.show()
