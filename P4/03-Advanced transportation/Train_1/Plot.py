import matplotlib.pyplot as plt
from scipy.optimize import linprog, minimize
import sympy as sp
import numpy as np
import seaborn as sns

class Plot:
    def __init__(self, title="Coordinate Plot", use_seaborn=False):
        """Initializes the plot object with an optional seaborn styling."""
        self.title = title
        self.lines = []  # List to store lines (sympy expressions)
        self.points = []  # List to store points (as tuples with optional labels)
        self.fig, self.ax = plt.subplots()
        
        if use_seaborn:
            sns.set(style="whitegrid")
        
        self._setup_plot()  # Private method to set up plot

    def _setup_plot(self):
        """Private method to set up initial plot properties."""
        self.ax.set_title(self.title)
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.axhline(0, color='black',linewidth=0.5)
        self.ax.axvline(0, color='black',linewidth=0.5)
        self.ax.grid(True)

    def add_line(self, sympy_expr, label=None):
        """Adds a mathematical line based on a sympy equation."""
        x = sp.symbols('x')
        f_lambdified = sp.lambdify(x, sympy_expr, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambdified(x_vals)
        
        line, = self.ax.plot(x_vals, y_vals, label=label)
        self.lines.append((sympy_expr, line))
        
        if label:
            self.ax.legend()

    def add_point(self, x, y, label=None):
        """Adds a point (or node) to the plot."""
        self.points.append((x, y, label))
        self.ax.scatter(x, y, label=label, zorder=5)
        
        if label:
            self.ax.text(x, y, f' {label}', fontsize=12)

    def add_segment(self, x1, y1, x2, y2, label=None):
        """Adds a line segment between two points."""
        self.ax.plot([x1, x2], [y1, y2], marker = 'o')
        if label:
            self.ax.text((x1 + x2) / 2, (y1 + y2) / 2, f'{label}', fontsize=12)

    def add_inequality(self, sympy_ineq, label=None):
        """
        Adds and shades the region for an inequality.
        sympy_ineq should be a sympy inequality object like 12*x + 2*y <= 12.
        """
        x, y = sp.symbols('x y')
        
        # Handle vertical lines (x-related inequalities)
        if sympy_ineq.has(x) and not sympy_ineq.has(y):
            x_val = sp.solve(sympy_ineq.lhs - sympy_ineq.rhs, x)
            if x_val:
                x_val = float(x_val[0])  # Convert to numerical value
                self.ax.axvline(x=x_val, label=label, color='blue', linestyle='--')
                if isinstance(sympy_ineq, sp.LessThan):
                    self.ax.fill_betweenx(np.linspace(-10, 10, 400), x_val, -10, alpha=0.3)
                elif isinstance(sympy_ineq, sp.GreaterThan):
                    self.ax.fill_betweenx(np.linspace(-10, 10, 400), x_val, 10, alpha=0.3)
            return

        # Handle horizontal lines (y-related inequalities)
        if sympy_ineq.has(y) and not sympy_ineq.has(x):
            y_val = sp.solve(sympy_ineq.lhs - sympy_ineq.rhs, y)
            if y_val:
                y_val = float(y_val[0])  # Convert to numerical value
                self.ax.axhline(y=y_val, label=label, color='green', linestyle='--')
                if isinstance(sympy_ineq, sp.LessThan):
                    self.ax.fill_between(np.linspace(-10, 10, 400), y_val, -10, alpha=0.3)
                elif isinstance(sympy_ineq, sp.GreaterThan):
                    self.ax.fill_between(np.linspace(-10, 10, 400), y_val, 10, alpha=0.3)
            return

        # For general inequalities, solve for y in terms of x
        try:
            inequality_func = sp.solve(sympy_ineq.lhs - sympy_ineq.rhs, y)
            if inequality_func:
                inequality_func = inequality_func[0]  # Get the first solution for y
            else:
                raise ValueError("Cannot solve for y")
        except Exception as e:
            print(f"Could not solve for y in inequality {sympy_ineq}: {e}")
            return

        # Lambdify the function for fast numerical evaluation
        f_lambdified = sp.lambdify(x, inequality_func, 'numpy')

        # Get a range of x values for plotting
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambdified(x_vals)

        # Ensure that y_vals are numerical and finite
        y_vals = np.array([float(y) if np.isfinite(y) else np.nan for y in y_vals])

        # Plot the boundary line
        line, = self.ax.plot(x_vals, y_vals, label=label)

        # Determine the inequality type and shade the area accordingly
        if isinstance(sympy_ineq, sp.LessThan):
            self.ax.fill_between(x_vals, y_vals, y_vals - 10, where=(y_vals <= 10), alpha=0.3)
        elif isinstance(sympy_ineq, sp.GreaterThan):
            self.ax.fill_between(x_vals, y_vals, y_vals + 10, where=(y_vals >= -10), alpha=0.3)

    def plot_optimization(self, objective_func, boundaries, bounds_type='ineq', minimize_obj=True):
        """
        Plots a 2D optimization problem with the objective function and boundary constraints.
        
        Parameters:
            - objective_func: A sympy function or expression for the objective (e.g., 3*x + 2*y).
            - boundaries: A list of sympy inequality constraints (e.g., [12*x + 2*y <= 12, x >= 0]).
            - bounds_type: Specifies 'ineq' for inequalities or 'eq' for equalities.
            - minimize_obj: Boolean to indicate if the objective function should be minimized (True) or maximized (False).
        """
        x, y = sp.symbols('x y')
        
        # 1. Plot boundaries (like the add_inequality method)
        for boundary in boundaries:
            self.add_inequality(boundary, label=f'{boundary}')

        # 2. Define the objective function
        obj_func = sp.lambdify((x, y), objective_func, 'numpy')

        # 3. Create a grid of x and y values to plot contour of objective function
        x_vals = np.linspace(-10, 10, 400)
        y_vals = np.linspace(-10, 10, 400)
        X, Y = np.meshgrid(x_vals, y_vals)
        Z = obj_func(X, Y)
        
        # Plot contours of the objective function
        contour = self.ax.contour(X, Y, Z, levels=20, cmap="coolwarm", alpha=0.6)
        self.ax.clabel(contour, inline=True, fontsize=8)

        # 4. Optimize the objective function
        def objective(xy):
            return obj_func(xy[0], xy[1])

        # Define bounds based on constraints
        # Here we assume boundaries are linear inequalities in the form of Ax <= b
        cons = []
        for boundary in boundaries:
            lhs = boundary.lhs
            rhs = boundary.rhs
            
            # Convert sympy expressions to callable functions for scipy constraints
            lhs_func = sp.lambdify((x, y), lhs, 'numpy')
            rhs_func = sp.lambdify((x, y), rhs, 'numpy')
            
            # Form scipy-style inequality constraints
            if isinstance(boundary, sp.LessThan):
                cons.append({'type': 'ineq', 
                            'fun': lambda xy, lhs=lhs_func, rhs=rhs_func: float(rhs(xy[0], xy[1])) - float(lhs(xy[0], xy[1]))})
            elif isinstance(boundary, sp.GreaterThan):
                cons.append({'type': 'ineq', 
                            'fun': lambda xy, lhs=lhs_func, rhs=rhs_func: float(lhs(xy[0], xy[1])) - float(rhs(xy[0], xy[1]))})

        
        # Run optimization (minimization or maximization)
        if minimize_obj:
            result = minimize(objective, x0=[0, 0], constraints=cons)
        else:
            result = minimize(lambda xy: -objective(xy), x0=[0, 0], constraints=cons)

        # Get the optimal point
        opt_point = result.x
        opt_value = objective(opt_point)

        # 5. Plot the optimal point
        self.ax.scatter(opt_point[0], opt_point[1], color='red', marker='*', s=100, label=f'Optimum: {opt_value:.2f}')
        self.ax.text(opt_point[0], opt_point[1], f'({opt_point[0]:.2f}, {opt_point[1]:.2f})', fontsize=12)

        # Add the legend at the end to include all labels
        self.ax.legend()


    def set_plot_limits(self, x_min, x_max, y_min, y_max):
        """
        Adjust the scale of the plot to fit within the specified boundaries.

        Parameters:
        - x_min: Minimum x-coordinate of the visible area.
        - x_max: Maximum x-coordinate of the visible area.
        - y_min: Minimum y-coordinate of the visible area.
        - y_max: Maximum y-coordinate of the visible area.
        """
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
        self.ax.figure.canvas.draw()  # Redraw the plot to apply the changes

    def show(self):
        """Displays the plot."""
        plt.show()
        
    def save(self, filename):
        """Saves the plot to a file."""
        self.fig.savefig(filename)

