import numpy as np


class Point():
    def __init__(self, x: float, y: float, number) -> None:
        """
        It defines a point in 2D
        :param x: x component
        :param y: y component
        :param number: the number of element to specifying it.
        """
        self.x = x
        self.y = y
        self.number = str(number)


class Element():
    def __init__(self, node1: Point, node2: Point, A: float, E: float):
        """
        It specifies an element in 2D
        :param node1: starts with a node1
        :param node2: ends with a node2
        :param E: elasticities modul
        :param A: Area of element
        """
        self.start = node1.number
        self.end = node2.number
        self.E = E
        self.L = cal_lenth(node1, node2)
        self.A = A

    def make_element_K_with_help(self, node1: Point, node2: Point) -> None:
        """
        It produces a matrix as K for The Element.
        !!! if need you can change the "freedom" list to change the result for different situations !!!
        :param node1: start node1.
        :param node2: end node2.
        :return now you can use "element.K" and "element.K_help".
        """
        cos = (node2.x - node1.x) / self.L
        sin = (node2.y - node1.y) / self.L
        temp = (self.A * self.E) / self.L
        K = ((self.A * self.E) / self.L) * np.array(
            [cos ** 2, sin * cos, -cos ** 2, -cos * sin, cos * sin, sin ** 2, -cos * sin, -sin ** 2,
             -cos ** 2, -cos * sin, cos ** 2, cos * sin, -cos * sin, -sin ** 2, cos * sin, sin ** 2])

        K_help = np.array([])
        freedom = ["x", "y"]
        for i in range(len(freedom)):
            for j in range(len(freedom)):
                K_help = np.append(K_help, node1.number + freedom[i] + node1.number + freedom[j])
            for j in range(len(freedom)):
                K_help = np.append(K_help, node1.number + freedom[i] + node2.number + freedom[j])
        for i in range(len(freedom)):
            for j in range(len(freedom)):
                K_help = np.append(K_help, node2.number + freedom[i] + node1.number + freedom[j])
            for j in range(len(freedom)):
                K_help = np.append(K_help, node2.number + freedom[i] + node2.number + freedom[j])

        self.K = K
        self.K_help = K_help

    def merge_K(self, K, K_help):
        """
        assembling function. it should use for every element separately.
        :param K: The main K that will be total.
        :param K_help: the help matrix to total K.
        :return: total K
        """
        for p, v in np.ndenumerate(K_help):
            for p2, v2 in np.ndenumerate(self.K_help):
                if v == v2:
                    K[p] += self.K[p2]
        return K

    def __repr__(self, K=True):
        if K == True:
            return str(self.K)
        else:
            pass


def cal_lenth(node1, node2) -> float:
    """
    calculate the lenth with two point
    """
    return np.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


def make_K_help(n: int, start_one: int = 1, start_two: int = 1) -> list:
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
                    if len(str(k)) == 1 and len(str(k2)):
                        K_help = np.append(K_help, "0" + str(k) + freedom[i] + "0" + str(k2) + freedom[j])
                    elif len(str(k)) == 1:
                        K_help = np.append(K_help, "0" + str(k) + freedom[i] + str(k2) + freedom[j])
                    elif len(str(k2)) == 1:
                        K_help = np.append(K_help, str(k) + freedom[i] + "0" + str(k2) + freedom[j])
                    else:
                        K_help = np.append(K_help, str(k) + freedom[i] + str(k2) + freedom[j])
    return K_help
