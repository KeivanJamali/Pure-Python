import numpy as np


class Point:
    def __init__(self, x: float, y: float, number) -> None:
        """
        It defines a point in 2D
        :param x: x component
        :param y: y component
        :param number: the number of element to specifying it.
        """
        self.x = x
        self.y = y
        if type(number) == int:
            self.number = str(number)
        elif type(number) == str:
            self.number = number
        else:
            raise TypeError


class Element:
    def __init__(self, node1: Point, node2: Point, A: float, E: float):
        """
        It specifies an element in 2D
        :param node1: starts with a node1
        :param node2: ends with a node2
        :param E: elasticities modul
        :param A: Area of element
        """
        self.K_help = None
        self.K = None
        self.node1 = node1
        self.node2 = node2
        self.start = node1.number
        self.end = node2.number
        self.E = E
        self.L = cal_length(node1, node2)
        self.A = A
        self.make_element_K_with_help()

    def make_element_K_with_help(self) -> None:
        """
        It produces a matrix as K for The Element.
        !!! if need you can change the "freedom" list to change the result for different situations !!!
        :return now you can use "element.K" and "element.K_help".
        """
        cos = (self.node2.x - self.node1.x) / self.L
        sin = (self.node2.y - self.node1.y) / self.L
        K = ((self.A * self.E) / self.L) * np.array(
            [cos ** 2, sin * cos, -cos ** 2, -cos * sin, cos * sin, sin ** 2, -cos * sin, -sin ** 2,
             -cos ** 2, -cos * sin, cos ** 2, cos * sin, -cos * sin, -sin ** 2, cos * sin, sin ** 2])

        K_help = np.array([])
        freedom = ["x", "y"]
        for i in range(len(freedom)):
            for j in range(len(freedom)):
                K_help = np.append(K_help, self.start + freedom[i] + self.start + freedom[j])
            for j in range(len(freedom)):
                K_help = np.append(K_help, self.start + freedom[i] + self.end + freedom[j])
        for i in range(len(freedom)):
            for j in range(len(freedom)):
                K_help = np.append(K_help, self.end + freedom[i] + self.start + freedom[j])
            for j in range(len(freedom)):
                K_help = np.append(K_help, self.end + freedom[i] + self.end + freedom[j])

        self.K = K
        self.K_help = K_help

    def merge_K(self, total_k, k_help):
        """
        assembling function. it should use for every element separately.
        :param total_k: The main K that will be total.
        :param k_help: the help matrix to total K.
        :return: total K
        """
        for p, v in np.ndenumerate(k_help):
            for p2, v2 in np.ndenumerate(self.K_help):
                if v == v2:
                    total_k[p] += self.K[p2]
        return total_k

    def __repr__(self, K=True):
        if K:
            return str(self.K)
        else:
            pass


def cal_length(node1, node2) -> float:
    """
    calculate the length with two point
    """
    return np.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


def make_K_help(n: int, start_one: int = 1, start_two: int = 1) -> np.array:
    """
    it will produce a matrix with name for each place to help for Boundary conditions. And also for total K. changeable!!!
    :param n: matrix rows or columns
    :param start_one: the pre number for first element will start with this
    :param start_two: the pre number for second element will start with this
    :return: a matrix which is a help matrix to know the positions
    """
    freedom = ["x", "y"]  # here is the freedom, and it can change in future!
    n //= len(freedom)
    K_help = np.array([])
    for k in range(start_one, n + start_one):
        for i in range(len(freedom)):
            for k2 in range(start_two, n + start_two):
                for j in range(len(freedom)):
                    K_help = np.append(K_help, str(k) + freedom[i] + str(k2) + freedom[j])

    return K_help
