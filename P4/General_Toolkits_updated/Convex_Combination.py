import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from scipy.optimize import minimize_scalar


class ConvexCombinationOptimizer:
    def __init__(self, objective_function, params:list, constraint_set:list, equality:list, parameters:list):
        self.objective_function = objective_function
        self.params = params
        self.parameters = parameters # only use for Simplextep function
        self.equality = equality # only use for Simplextep function
        self.gradian_function = [sp.diff(objective_function, var) for var in params]
        self.history = {}
        self.constraints = constraint_set or []

    def _evaluate_gradient(self, point: list) -> list:
        subs = dict(zip(self.params, point))
        return [g.evalf(subs=subs) for g in self.gradian_function]

    def _solve_linearized_subproblem(self, gradian: list, x0: list) -> list:
        def find_objective(gradian, x0):
            objective_function = []
            for i in range(len(gradian)):
                objective_function.append(gradian[i])
            return objective_function
        
        problem = LinearProblemSolver(objective_coeffs=find_objective(gradian, x0),
                                      constraints=self.constraints,
                                      equality=self.equality,
                                      parameters=self.parameters)
        y, z = problem.solve()
        return y
    
    def _find_step(self, point, y):
        direction = [y_i - x_i for y_i, x_i in zip(y, point)]

        # Create symbolic expression for phi(α)
        alpha = sp.Symbol('alpha', real=True)
        new_point_expr = [x + alpha * d for x, d in zip(point, direction)]
        phi_expr = self.objective_function.subs(dict(zip(self.params, new_point_expr)))
        
        # Lambdify for numeric search
        phi_func = sp.lambdify(alpha, phi_expr, 'numpy')

        # Use scipy to find alpha in [0, 1]
        result = minimize_scalar(phi_func, bounds=(0, 1), method='bounded')

        alpha_star = result.x if result.success else 0.1  # fallback step size
        return alpha_star

    def fit(self, x0: list, lr:float, error=1e-6, max_iter=100):
        x0 = list(map(float, x0))

        for i in range(max_iter):
            gradian = self._evaluate_gradient(x0)
            self.history[i] = list(x0)

            # Solve linearized subproblem
            y = self._solve_linearized_subproblem(gradian, x0)
            x_old = x0

            step_size = lr if lr else self._find_step(point=x0, y=y)
            
            x0 = [x + step_size * (s - x) for x, s in zip(x0, y)]
            criteria = sum([abs(t0 - t1) for t0, t1 in zip(x0, x_old)])
            print(f"[INFO] step {i} : x = {x0}")

            if criteria < error:
                print(f"[Success] Converged in {i} iterations.")
                return x0

        print("[ERROR] Reached max iterations.")
        return x0
    
    def plot_contour(self, xlim=(-5, 5), ylim=(-5, 5), resolution=100):
        # Prepare meshgrid
        x_vals = np.linspace(xlim[0], xlim[1], resolution)
        y_vals = np.linspace(ylim[0], ylim[1], resolution)
        X, Y = np.meshgrid(x_vals, y_vals)
        
        # Lambdify the symbolic function for NumPy use
        f_lambdified = sp.lambdify((self.params[0], self.params[1]), self.objective_function, 'numpy')
        Z = f_lambdified(X, Y)

        # Plot contour
        plt.figure(figsize=(10, 8))
        plt.contour(X, Y, Z, levels=50, cmap='viridis')
        plt.colorbar(label='Function Value')
        
        # Extract history points
        xs = [float(p[0]) for p in self.history.values()]
        ys = [float(p[1]) for p in self.history.values()]
        
        # Plot points and path
        plt.plot(xs, ys, 'ro--', label='Descent Path')
        plt.scatter(xs[0], ys[0], color='blue', label='Start')
        plt.scatter(xs[-1], ys[-1], color='green', label='End (Min)')

        for i in range(len(xs)-1):
            plt.arrow(xs[i], ys[i],
                    xs[i+1] - xs[i], ys[i+1] - ys[i],
                    head_width=0.1, length_includes_head=True, color='red')

        plt.title('Steepest Descent Path')
        plt.xlabel(str(self.params[0]))
        plt.ylabel(str(self.params[1]))
        plt.legend()
        plt.grid(True)
        plt.savefig("figs\convex_steps.png")
        plt.show()




class LinearProblemSolver:
    def __init__(self, objective_coeffs: list, constraints: list, equality: list, parameters: list):
        self.c = np.array(objective_coeffs, dtype=np.float64)
        self.constraints = constraints
        self.equality = equality
        self.param_info = parameters

    def _build_constraints(self):
        A_ub = []
        b_ub = []

        for (rhs, *lhs), eq in zip(self.constraints, self.equality):
            coeffs = np.array(lhs, dtype=np.float64)
            if eq == "leq":
                A_ub.append(coeffs)
                b_ub.append(rhs)
            elif eq == "geq":
                A_ub.append(-coeffs)
                b_ub.append(-rhs)
            else:
                raise ValueError(f"Unsupported constraint type: {eq}")

        return np.array(A_ub), np.array(b_ub)

    def _build_bounds(self):
        bounds = []
        for name, sign in self.param_info:
            if sign == "+":
                bounds.append((0, None))  # x >= 0
            elif sign == "n":
                bounds.append((None, None))  # unrestricted
            elif sign == "-":
                bounds.append((None, 0)) # x <= 0
            else:
                raise ValueError(f"Unsupported sign for parameter {name}: {sign}")
        return bounds

    def solve(self):
        A_ub, b_ub = self._build_constraints()
        bounds = self._build_bounds()
        result = linprog(self.c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

        if result.success:
            return result.x, result.fun
        else:
            raise RuntimeError("Linear optimization failed: " + result.message)
