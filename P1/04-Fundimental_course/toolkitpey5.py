import numpy as np


class Point():
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


def iz_max(qbar: float, q: float, qz: float) -> float:
    """
    :param qbar: main q
    :param q: layer pressure (KPa)
    :param qz: pressure till z (KPa)
    :return: Iz(m)
    """
    result = 0.5 + 0.1 * ((qbar - q) / qz) ** 0.5
    return result


def point_between(point1: Point, point2: Point, x: float) -> float:
    """
    you give it x as input, and it gives you y, based on the line between point1 and point2.
    """
    m = (point2.y - point1.y) / (point2.x - point1.x)
    y = m * (x - point1.x) + point1.y
    return y


def Es(L: float, B: float, qc: float) -> float:
    """
    Schmertmann solution.
    :param L: length of pey(higher) (m)
    :param B: width of pey(lower) (m)
    :param qc: cone penetration resistance (KPa)
    :return: Es (KPa)
    """
    if L / B >= 10:
        ES = 3.5 * qc
        return ES
    elif B - L < 0.1:
        ES = 2.5 * qc
        return ES
    else:
        if L / B >= 10:
            ES = 3.5 * qc
            return ES
        else:
            ES = 2.5 * qc
        result = (1 + 0.4 * np.log10(L / B)) * ES
        return result


def c1_Schmertmann(q: float, qbar: float) -> float:
    """
    :param q: effective stress(gama*Df) (KPa)
    :param qbar: stress at the level of foundation (KPa)
    :return: c1
    """
    result = 1 - 0.5 * q / (qbar - q)
    return result


def c2_Schmertmann(t: float) -> float:
    """
    :param t: time in years
    :return: c2
    """
    return 1 + 0.2 * np.log10(t / 0.1)


def alfa_embank(b1: float, b2: float, z: float, q0: float = 1) -> list:
    """
    returns a list contains alfa1, alfa2, sigma
    :param b1: top length (m)
    :param b2: triangle bottom length (m)
    :param z: depth (m)
    :param q0: presser in KPa - default is 1
    :return: alfa1 and alfa2 in radian (Ra) and sigma (KPa)
    """
    alfa1 = np.arctan((b1 + b2) / z) - np.arctan(b1 / z)
    alfa2 = np.arctan(b1 / z)
    sigma = (q0 / np.pi) * ((((b1 + b2) / b2) * (alfa2 + alfa1)) - (b1 * alfa2 / b2))
    return [alfa1, alfa2, sigma]


class Elastic_settlement():
    def __init__(self, u: float, Es: float):
        """
        :param u: miu
        :param Es: (KPa)
        """
        self.u = u
        self.Es = Es

    def Is_calculation(self, F1: float, F2: float):
        return F1 + (1 - 2 * self.u) / (1 - self.u) * F2

    def Se_calculation(self, q0: float, a: int, B_prime: float, Is: float, If: float, rigid: bool = False):
        """
        :param q0: (KPa)
        :param a: 4 if center --- 1 if corner
        :param B_prime: B/2 for center --- B for corner
        :return: settlement in (mm)
        """
        Se_fel = q0 * a * B_prime * ((1 - self.u ** 2) / self.Es) * Is * If
        if rigid == False:
            return Se_fel * 1000
        else:
            return Se_fel * 0.93 * 1000
