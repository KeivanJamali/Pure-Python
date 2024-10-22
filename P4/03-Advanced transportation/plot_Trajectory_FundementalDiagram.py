import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import seaborn as sns


class Plot_FD:
    def __init__(self, title="Fundamental Diagram", sensivity:int=500):
        self.title = title
        self.lines_data = {}
        self.lines = {}
        self.diagrams = {}
        self.sensivity = sensivity
        self.points = {}
        self._setup_plot()  # Set up initial plot properties

    def _setup_plot(self):
        """Private method to set up initial plot properties."""
        plt.title(self.title)
        plt.xlabel('K (Cars/Length)')
        plt.ylabel('Q (Cars/Time)')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True)

    def get_one_diagram(self, title:str, line1, line2, write_intersection:bool=False):
        """Adds a mathematical line based on a sympy equation."""
        if title in self.diagrams.keys():
            raise KeyError("Same title. It is not possiable.")
        else:
            self.diagrams[title] = {}
        x = sp.symbols('x')
        intersection_x = sp.solve(line1 - line2, x)
        intersection_y = line1.subs(x, intersection_x[0])
        intersection_x = intersection_x[0]
        print(f"Intersection point: x = {intersection_x:.2f}, y = {intersection_y:.2f}")
        y_zero = sp.solve(line2, x)[0]

        f_lambdified1 = sp.lambdify(x, line1, 'numpy')
        f_lambdified2 = sp.lambdify(x, line2, 'numpy')
        x_vals1 = np.linspace(0, intersection_x, self.sensivity)
        y_vals1 = f_lambdified1(x_vals1)
        x_vals2 = np.linspace(intersection_x, y_zero, self.sensivity)
        y_vals2 = f_lambdified2(x_vals2)

        plt.plot(x_vals1, y_vals1, label=f"Slope = {(f_lambdified1(x_vals1[-1])-f_lambdified1(x_vals1[0]))/(x_vals1[-1]-x_vals1[0]):.2f}")
        self.lines_data[title+"1"] = [x_vals1, y_vals1]
        self.lines[title+"1"] = line1
        plt.plot(x_vals2, y_vals2, label=f"Slope = {(f_lambdified2(x_vals2[-1])-f_lambdified2(x_vals2[0]))/(x_vals2[-1]-x_vals2[0]):.2f}")
        self.lines_data[title+"2"] = [x_vals2, y_vals2]
        self.lines[title+"2"] = line2

        plt.scatter(float(intersection_x), float(intersection_y), color='black', zorder=5)
        if write_intersection:
            plt.text(float(intersection_x)*1.4, float(intersection_y)*0.9, 
                     f"({float(intersection_x):.0f}, {float(intersection_y):.0f})", 
                     fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='black')
        plt.legend()
        self.diagrams[title]["Q_max"] = f_lambdified1(x_vals1[-1])
        self.diagrams[title]["K_opt"] = intersection_x
        self.diagrams[title]["K_jam"] = y_zero
        self.diagrams[title]["Free flow speed"] = (f_lambdified1(x_vals1[-1])-f_lambdified1(x_vals1[0]))/(x_vals1[-1]-x_vals1[0])
        self.diagrams[title]["If from conjected to max slop"] = (f_lambdified2(x_vals2[-1])-f_lambdified2(x_vals2[0]))/(x_vals2[-1]-x_vals2[0])
        plt.draw()

    def set_plot_limits(self, x_min, x_max, y_min, y_max):
        """Adjust the scale of the plot to fit within the specified boundaries."""
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.draw()  # Redraw the plot to apply the changes

    def save_fig(self, name):
        plt.savefig(f"{name}.svg")


class Plot_Trajectory:
    def __init__(self, title="Trajectory", sensitivity=2):
        self.title = title
        self.sensitivity = sensitivity
        self.lines_data = {}
        self.lines = {}
        self.intervals = []
        self.i = -1
        self.x = sp.symbols("x")


    def make_trajectory(self, constant_speed, density, end_time, end_x=None):
        """
        Gather trajectory parameters.
        
        Parameters:
        - start_x: Starting x-coordinate
        - end_x: Ending x-coordinate
        - start_time: Starting time
        - end_time: Ending time
        - constant_speed: A constant speed for the cars
        - density: Density of the street (cars per unit length)
        """
        self.i += 1
        self.lines_data[str(self.i)] = []
        self.lines[str(self.i)] = []


        self._defind_lines_formula(constant_speed=constant_speed, density=density, start_time=0, start_x=0,
                                   end_time=end_time, end_x=end_x)
        

    def _defind_lines_formula(self, constant_speed, density, start_time, start_x, end_time, end_x):
        slop = constant_speed
        if density == 0:
            raise ZeroDivisionError("Density is Zero now.")
        spacing = 2000/(density)
        if self.i >= 1:
            line_temp = self.lines[str(self.i-1)][0]
            start_time = line_temp[1][1].x
            end_x = line_temp[0].subs(self.x, line_temp[1][1].x)
            

        p0 = Point(start_time, start_x)
        p1 = Point(end_time, end_x)
        i = 0
        while (i * spacing) < (p1.y - p0.y):
            line = slop*(self.x - p0.x) + p1.y - spacing * i
            self.lines[str(self.i)].append([line, (p0, p1)])
            i += 1

    def intersections_maker(self):
        self.inter_did = True
        zones = [str(i) for i in range(len(self.lines))]
        number_of_lines = []
        for k, v in self.lines.items():
            print(f"[INFO] We plot zone {int(k)+1} with {len(v)} lines...")
            number_of_lines.append(len(v))
        self.number_of_lines = min(number_of_lines)

        for step in range(self.number_of_lines):
            for i in range(len(zones)-1):
                intersection_x = sp.solve(self.lines[zones[i]][step][0] - self.lines[zones[i+1]][step][0], self.x)
                intersection_x = intersection_x[0] if intersection_x else 0
                self.lines[zones[i]][step].append(intersection_x)
                self.lines[zones[i+1]][step].append(intersection_x)

    def fit_data(self, plot=True):
        if not self.inter_did:
            raise Exception("[ERROR] First run the intersections_maker function.")
        for k, v in self.lines.items():
            self.lines_data[k] = []
            for line_i in range(self.number_of_lines):
                if k == "0":
                    x_values = np.linspace(v[line_i][1][0].x, v[line_i][2], self.sensitivity)
                    f_lambdified = sp.lambdify(self.x, v[line_i][0], 'numpy')
                    y_values = f_lambdified(x_values)
                    self.lines_data[k].append([x_values, y_values])
                elif k == str(len(self.lines)-1):
                    x_values = np.linspace(v[line_i][2], v[line_i][1][1].x, self.sensitivity)
                    f_lambdified = sp.lambdify(self.x, v[line_i][0], 'numpy')
                    y_values = f_lambdified(x_values)
                    self.lines_data[k].append([x_values, y_values])
                else:
                    x_values = np.linspace(v[line_i][2], v[line_i][3], self.sensitivity)
                    f_lambdified = sp.lambdify(self.x, v[line_i][0], 'numpy')
                    y_values = f_lambdified(x_values)
                    self.lines_data[k].append([x_values, y_values])
        if plot:
            self._plot_trajectory()

    def _plot_trajectory(self):
        plt.figure(figsize=(10, 6))
        plt.title(self.title)
        plt.ylabel('Distance (x)')
        plt.xlabel('Time (t)')

        for k, v in self.lines_data.items():
            for line in v:
                k = int(k)
                plt.plot(line[0], line[1])
        plt.grid()
        plt.show()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y