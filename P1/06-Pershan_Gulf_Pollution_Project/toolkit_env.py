import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


class Point:
    def __init__(self, x: float, y: float = 0, z: float = 0, c: float = 0):
        """
        :param x: x component.
        :param y: y component.
        :param z: z component.
        :param c: concentration in point.
        """
        self.x = x
        self.y = y
        self.z = z
        self.c = c


class Transport:
    def __init__(self, m: float, Dx: float, Dy: float = False, Dz: float = False):
        """
        :param m: the amount of pollute as kg.
        :param Dx: Coefficient in x direction.
        :param Dy: Coefficient in y direction.
        :param Dz: Coefficient in z direction.
        """
        self.m = m
        self.dx = Dx
        self.dy = Dy
        self.dz = Dz

    def diffusion(self, dimension: int, t: float, x: float, y: float = False, z: float = False, L: float = False,
                  A: float = False) -> float:
        """
        It will give you the concentration as c
        :param dimension: what space are you working at? 1d or 2d or 3d. just write the number only.
        :param t: at what time are you looking at it. (s)
        :param L: if you are in 2d (m)
        :param A: if you are in 1d (m^2)
        :return: concentration
        """
        if dimension == 1:
            c = (self.m / (A * np.sqrt(4 * np.pi * self.dx * t))) * (np.exp(-((x ** 2) / (4 * self.dx * t))))
        elif dimension == 2:
            c = (self.m / (L * 4 * np.pi * t * np.sqrt(self.dx * self.dy))) * (
                np.exp(-((x ** 2) / (4 * self.dx * t)) - ((y ** 2) / (4 * self.dy * t))))
        elif dimension == 3:
            c = (self.m / (4 * np.pi * t * np.sqrt(4 * np.pi * self.dx * self.dy * self.dz * t))) * (
                np.exp(-((x ** 2) / (4 * self.dx * t)) - ((y ** 2) / (4 * self.dy * t)) - (
                        (z ** 2) / (4 * self.dz * t))))
        else:
            print("Wrong dimension. you should enter 1 or 2 or 3.")
        return c


def plot_picture(t: float, nodes, vx: float = 0, vy: float = 0, error: float = 1, scale: float = 5, split: int = None,
                 iteration: int = -1, color=None, scenario: int = 1, show: bool = True, save: bool = True,
                 detail: bool = True):
    """
    it will plot for you!
    :param color: set of color1 for plotting. it should be at list 1000 number!
    :param t: what time is it??!
    :param nodes: give it the nodes at time t.
    :param vx: x component of vector speed.
    :param vy: y component of vector speed.
    :param error: how exact do you like to be. it will took time also. default = 1. you shouldn't give it split, unless it will ignore your Error and calculate it itself...
    :param scale: in what scale are you looking at. the result will be for example if scale is 5 -> square from -5 to 5(10 * 10)
    :param split: how many times you want you scale concentration?
    :param scenario: if you like to save it better, put a number which will show for the save name in png file
    :param show: if you want to see the plot type True. unless False
    :param save: if you want to save the figure type True. unless False
    :param detail: if you want to get some more information
    :return: it will plot for you!
    """
    x_list = []
    y_list = []
    c_list = []
    max_c = 0
    for i in nodes:
        if i.c > max_c:
            max_c = i.c
    if split == None:
        temp = int(np.around(1 / (2 * error)))
        split = int(np.around(temp * max_c))
    else:
        temp = split // max_c
        error = 0.5 * (1 / temp)
    if detail:
        print("split is: ", split, "\nmax_c is: ", max_c, "\ntemp is: ", temp, "\nerror is: ", error)
    for i in range(split):
        i /= temp
        iteration += 1
        x_list.append([])
        y_list.append([])
        c_list.append([])
        for j in nodes:
            if abs(j.c - i) < error:
                if j.x + vx * t > scale:
                    x_list[iteration].append(j.x + vx * t - 2 * scale)
                elif j.x + vx * t < -scale:
                    x_list[iteration].append(j.x + vx * t + 2 * scale)
                else:
                    x_list[iteration].append(j.x + vx * t)

                if j.y + vy * t > scale:
                    y_list[iteration].append(j.y + vy * t - 2 * scale)
                elif j.y + vy * t < -scale:
                    y_list[iteration].append(j.y + vy * t + 2 * scale)
                else:
                    y_list[iteration].append(j.y + vy * t)
                c_list[iteration].append(j.c)
        if i > 0.00000001:
            plt.scatter(x_list[iteration], y_list[iteration], c=color[iteration])
        else:
            plt.scatter(x_list[iteration], y_list[iteration], c="#2874A6")

    plt.title(f"scenario {scenario}: at time {t:.2f} hour")
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    cmap = plt.get_cmap("nipy_spectral_r", split + 3)
    norm = mpl.colors.Normalize(vmin=0, vmax=6.5)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ticks=np.linspace(0, 6.5, 10))
    if save:
        plt.savefig(f"S{scenario} at {t:.2f}.png", dpi=300)
    if show:
        plt.show()
    plt.close()


def plot_curve(nodes: list, t: float, scenario: int = 1, show: bool = True, save: bool = True, vx: float = 0,
               vy: float = 0, scale: int = 5) -> None:
    """
    It will plot a cure for c in possession x and y
    :param nodes: tell me what you want to plot.
    :param t: it will be shown in docs when you save the fig. (in hour)
    :param scenario: it will be shown in docs when you save the fig.
    :param show: if you want to see the plot type True. unless False
    :param save: if you want to save the figure type True. unless False
    :param vx: x component of vector speed.
    :param vy: y component of vector speed.
    :param scale: in what scale are you looking at. the result will be for example if scale is 5 -> square from -5 to 5(10 * 10)
    :return: it will save or plot for you.
    """
    plt.style.use('seaborn-poster')
    x = []
    x2 = []
    y = []
    y2 = []
    c = []
    cx = []
    cy = []
    for i in range(len(nodes)):
        if nodes[i].x + vx * t > scale:
            x.append(nodes[i].x + vx * t - 2 * scale)
        elif nodes[i].x + vx * t < -scale:
            x.append(nodes[i].x + vx * t + 2 * scale)
        else:
            x.append(nodes[i].x + vx * t)

        if nodes[i].x == 0:
            if nodes[i].y + vy * t > scale:
                y2.append(nodes[i].y + vy * t - 2 * scale)
            elif nodes[i].y + vy * t < -scale:
                y2.append(nodes[i].y + vy * t + 2 * scale)
            else:
                y2.append(nodes[i].y + vy * t)
            cy.append(nodes[i].c)

        if nodes[i].y + vy * t > scale:
            y.append(nodes[i].y + vy * t - 2 * scale)
        elif nodes[i].y + vy * t < -scale:
            y.append(nodes[i].y + vy * t + 2 * scale)
        else:
            y.append(nodes[i].y + vy * t)

        if nodes[i].y == 0:
            if nodes[i].x + vx * t > scale:
                x2.append(nodes[i].x + vx * t - 2 * scale)
            elif nodes[i].x + vx * t < -scale:
                x2.append(nodes[i].x + vx * t + 2 * scale)
            else:
                x2.append(nodes[i].x + vx * t)
            cx.append(nodes[i].c)
        c.append(nodes[i].c)

    plt.clf()
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, c)
    plt.title(f"scenario {scenario}: at time {t:.2f} hour 3D plot(X-Y-C)")
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    if save:
        plt.savefig(f"3D S{scenario} at {t:.2f}.png", dpi=300)
    if show:
        plt.show()

    plt.clf()
    plt.plot(x2, cx)
    plt.title(f"scenario {scenario}: at time {t:.2f} hour 2D plot(X-C)")
    plt.xlabel("X (m)")
    plt.ylabel("C (kg/m^3)")
    plt.ylim([0, 6.5])
    if save:
        plt.savefig(f"2Dx S{scenario} at {t:.2f}.png", dpi=300)
    if show:
        plt.show()

    plt.clf()
    plt.plot(y2, cy)
    plt.title(f"scenario {scenario}: at time {t:.2f} hour 2D plot(Y-C)")
    plt.xlabel("Y (m)")
    plt.ylabel("C (kg/m^3)")
    plt.ylim([0, 6.5])
    if save:
        plt.savefig(f"2Dy S{scenario} at {t:.2f}.png", dpi=300)
    if show:
        plt.show()
    plt.close()
