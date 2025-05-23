import numpy as np
import sympy as sp
import networkx as nx
from itertools import combinations
from tqdm.auto import tqdm

class Engine:
    def __init__(self, graph:nx.Graph, student_number:str):
        self.solution = None
        self.seed = int(student_number[0: 3]) + int(student_number[5: 7]) * int(student_number[7:])
        self.demand = []
        self.demand.append(2 + abs(int(student_number[6]) + int(student_number[7]) + int(student_number[8])))
        self.demand.append(2 + abs(int(student_number[6]) - int(student_number[7])))
        self.demand.append(2 + abs(int(student_number[7]) - int(student_number[8])))

        self.link_number, self.x = sp.symbols("ID, x")
        core = (self.link_number * self.seed + (self.link_number ** 2)) % 997
        A = (core * 3 + 17) % 19 + 1
        B = (core * 5 + 11) % 19 + 1
        self.general_travel_time_function = A * self.x + B
        self.graph = graph

    def set_setting(self, origins:list, destinations:list):
        self.origins = origins
        self.destinations = destinations
        self._create_flow_variable()
        self._add_travel_times_initial_flows()
        self._add_OD()

    def _create_flow_variable(self):
        self.flow_vars = {}
        for u, v in self.graph.edges():
            var_name = "x_" + "{" + f"{u}-{v}" + "}"
            sym_var = sp.symbols(var_name, nonnegative=True)
            self.graph.edges[u, v]["var"] = sym_var
            self.flow_vars[(u, v)] = sym_var

    def _add_travel_times_initial_flows(self):
        for u, v, data in self.graph.edges(data=True):
            t_uv = self.general_travel_time_function.subs(self.link_number, data["ID"])
            t_uv = t_uv.subs(self.x, data["var"])
            self.graph.edges[u, v]["travel_time"] = t_uv
            self.graph.edges[u, v]["flows"] = []

    def _add_OD(self):
        j = -1
        z = -1
        for i in self.graph.nodes:
            if i in self.origins:
                j += 1
                self.graph.nodes[i]["production"] = self.demand[j]
            else:
                self.graph.nodes[i]["production"] = 0

            if i in self.destinations:
                z += 1
                self.graph.nodes[i]["attraction"] = sum(self.demand)
            else:
                self.graph.nodes[i]["attraction"] = 0

    def kuhn_tucker(self, method="SO"):
        self.od_pairs = [(o, d) for o in self.origins for d in self.destinations]
        self._find_all_paths_for_od()
        self._assign_f_to_edges()
        self.constraints = self._defined_constraints()
        self.lagrange_vars = self._create_lagrange_variables()
        self.all_vars = self.lagrange_vars.copy()
        if method == "UE":
            self._compute_integral_costs()
            self.objective_function = self._make_objective_funcion(method="UE")
        elif method == "SO":
            self.objective_function = self._make_objective_funcion(method="SO")

        self.lagrange = self.objective_function
        for i in range(len(self.lagrange_vars)):
            self.lagrange += self.lagrange_vars[i] * self.constraints[i]
        self.gradian = [sp.Eq(cons, 0) for cons in self.constraints]
        multiple_vars = []
        for (r, s, k), (f, path) in self.f_vars.items():
            g = sp.Eq(sp.diff(self.lagrange, f), 0)
            self.all_vars.append(f)
            multiple_vars.append(f)
            self.gradian.append(g)

        n = len(multiple_vars)
        i = 0
        while not self.solution:
            print(f"[INFO] Start solving the lagrange problem... Iteration {i}")
            chosed_vars = list(combinations(multiple_vars, i))
            print(f"[INFO] We need {len(chosed_vars)} times of solving system of equations to finish this step.")
            self.best = float("inf")
            for vars_i in tqdm(range(len(chosed_vars))):
                if not chosed_vars[vars_i]:
                    solution = sp.solve(self.gradian, self.all_vars, dict=False)   
                    if solution:
                        self.solution = self._check_solution(solution=solution)
                        break
                else:
                    gradian = [sp.Eq(cons, 0) for cons in self.constraints]
                    all_vars = self.lagrange_vars.copy()
                    for (r, s, k), (f, path) in self.f_vars.items():
                        if f not in chosed_vars[vars_i]:
                            g = sp.Eq(sp.diff(self.lagrange, f), 0)
                            all_vars.append(f)
                            gradian.append(g)

                    objective_function = self.objective_function
                    for v in chosed_vars[vars_i]:
                        gradian_refined = []
                        objective_function = objective_function.subs(v, 0)
                        for g in gradian:
                            gradian_refined.append(g.subs(v, 0))
                        gradian = gradian_refined.copy()

                    solution = sp.solve(gradian, all_vars, dict=False)
                    if solution:
                        solution = self._check_solution(solution=solution)
                        if solution:
                            value = float(self.objective_function.subs(solution).evalf(5))
                            if value < self.best:
                                self.best = value
                                self.solution = solution
                            print(f"[INFO] At iteration {i} with setting {chosed_vars[vars_i]} to zero, we get objective function equal to {self.objective_function.subs(solution).evalf(5)}")
            if self.solution:
                print(f"[INFO] The value of objective function is : {self.best:.2f}")
                print(f"[success] Finished calculations!")
            i += 1
        self.get_link_flows_travel_time(solution=self.solution)

    def _make_objective_funcion(self, method):
        if method == "SO":
            objective_function = 0
            for u, v in self.graph.edges():
                objective_function += self.graph.edges[u, v]["var"] * self.graph.edges[u, v]["travel_time"]
                objective_function = objective_function.subs(self.graph.edges[u, v]["var"], sum(self.graph.edges[u, v]["flows"]))
            return objective_function
        elif method == "UE":
            objective_function = 0
            for u, v in self.graph.edges():
                objective_function += self.graph.edges[u, v]["integral_expr"]
                objective_function = objective_function.subs(self.graph.edges[u, v]["var"], sum(self.graph.edges[u, v]["flows"]))
            return objective_function

    def _defined_constraints(self):
        constraints = []
        for (o, d) in self.od_pairs:
            cons = 0
            for (r, s, k), (f, path) in self.f_vars.items():
                if r == o and d == s:
                    cons += f
            constraints.append((self.graph.nodes[o]["production"] + (-1 * cons)))
        return constraints

    def _compute_integral_costs(self):
        integral_costs = {}
        w = sp.symbols('w', real=True, positive=True)  # integration dummy variable
        
        for u, v in self.graph.edges():
            t_uv = self.graph.edges[u, v]['travel_time']
            x_uv = self.graph.edges[u, v]['var']
            
            t_uv_w = t_uv.subs(x_uv, w)
            integral_expr = sp.integrate(t_uv_w, (w, 0, x_uv))
            self.graph.edges[u, v]["integral_expr"] = integral_expr

    def _find_all_paths_for_od(self):
        all_paths = {}
        for r, s in self.od_pairs:
            paths = nx.all_simple_paths(self.graph, source=r, target=s)
            all_paths[(r, s)] = paths
        self._create_path_flow_variables(all_paths)

    def _create_path_flow_variables(self, all_paths):
        self.f_vars = {}
        for (r, s), paths in all_paths.items():
            for k, path in enumerate(paths):
                var_name = "f_" + "{" + f"{r}-{s}" + "}" + "^" + f"{k}"
                self.f_vars[(r, s, k)] = [sp.symbols(var_name, nonnegative=True), path]
        print(f"[INFO] In this scenario we have {len(self.f_vars)} possable path.")

    def _assign_f_to_edges(self):
        for key, (f, path) in self.f_vars.items():
            for i in range(len(path)-1):
                self.graph.edges[path[i], path[i+1]]["flows"].append(f)

    def _create_lagrange_variables(self):
        lagrange_vars = []
        for o, d in self.od_pairs:
            var_name = "\lambda_" + "{" + f"{o}-{d}" + "}"
            lagrange_vars.append(sp.symbols(var_name, nonnegative=True))
        return lagrange_vars

    def get_link_flows_travel_time(self, solution, print_=True):
        for u, v in self.graph.edges():
            try:
                flow = sum(self.graph.edges[u, v]["flows"]).subs(solution)
                zero_subs = {symbol: 0 for symbol in flow.free_symbols}
                flow = float(flow.subs(zero_subs))
            except:
                flow = 0
            travel_time = self.graph.edges[u, v]["travel_time"].subs(self.graph.edges[u, v]["var"], flow)
            self.graph.edges[u, v]["flow_value"] = flow 
            self.graph.edges[u, v]["travel_time_value"] = travel_time 
            if print_:
                print(f"[Result] {self.graph.edges[u, v]["var"]} => x={flow:.1f}  --  t={travel_time:.1f}")

    def get_path_travel_time(self, print_=True):
        for (o, d, k), (f, path) in self.f_vars.items():
            if f in self.solution:
                if self.solution[f] > 0:
                    s = 0
                    for i in range(len(path)-1):
                        s += self.graph.edges[path[i], path[i+1]]["travel_time_value"]
                    if print_:
                        print(f"[Result] For flow {f} which has the following path, we have a total travel time of {s}")
                        print(f"[Continue] {path}")
                else:
                    if print_:
                        print(f"[Result] We assume 0 for flow {f} which has the following path.")
                        print(f"[Continue] {path}")

    def _refine_solution(self, solution):
        solution_new = {}
        for k, v in solution.items():
            zero_subs = {symbol: 0 for symbol in v.free_symbols}
            v = float(v.subs(zero_subs))
            solution_new[k] = v
        for v in self.all_vars:
            if not v in solution_new.keys():
                solution_new[v] = 0
        return solution_new
    
    def _check_solution(self, solution):
        solution_refined = self._refine_solution(solution=solution)
        if all(solution_refined[f] >= -0.1 for f in self.all_vars if f in solution_refined):
            print(f"[INFO] The value of objective function is : {self.objective_function.subs(solution_refined).evalf(5)}")
            print(f"[success] Finished calculations!")
            return solution_refined
        else:
            return None

    def convex_combination_method(self, error=0.001):
        self.error = error
        self.od_pairs = [(o, d) for o in self.origins for d in self.destinations]
        self._find_all_paths_for_od()
        self._assign_f_to_edges()

        x_0 = {}
        for u, v in self.graph.edges():
            x_0[self.graph.edges[u, v]["var"]] = 0
        print(f"[INFO] Algorithm starts right now...")
        self._update_travel_time(solution=x_0, print_=False)
        x_n = self._all_or_nothing(xn=x_0)
        print(f"[INFO] Initializing is finished.")
        while True:
            self._update_travel_time(solution=x_n, print_=False)
            y_n = self._all_or_nothing(xn=x_n)
            alpha = self._linear_search(xn=x_n, yn=y_n)
            x_nn = {k: x_n[k] + alpha * (y_n[k] - x_n[k]) for k in x_n}
            if self._check_convergence(xn=x_n, xnn=x_nn):
                break
            x_n = x_nn
        print(f"[INFO] The process is done!. The solution is ready.")
        self.solution = x_nn


    def _all_or_nothing(self, xn:dict):
        f_time_dict = self._find_each_path(print_=False)
        result = {}
        for (r, s), value in f_time_dict.items():
            best_time = float('inf')
            best_var = None
            for var, time in value.items():
                if time < best_time:
                    best_time = time
                    best_var = var
            result[(r, s)] = best_var
        fn = {}
        for (r, s, k), (f, path) in self.f_vars.items():
            fn[f] = 0
        for (r, s), var in result.items():
            fn[var] = self.graph.nodes[r]["production"]
        
        xn = self._make_x_from_f(f=fn)
        # print(fn)
        return xn
    
    def _linear_search(self, xn:dict, yn:dict) -> float:
        alpha = self._compute_integral_costs_convex_combination(xn=xn, yn=yn)
        objective_function = 0
        for u, v in self.graph.edges():
            objective_function += self.graph.edges[u, v]["integral_expr"]
        derivative = sp.diff(objective_function, alpha)
        critical_points = sp.solve(derivative, alpha)
        # critical_points = [pt for pt in critical_points if pt.is_real and pt >= 0]
        print(critical_points)
        return float(critical_points[0])

    def _compute_integral_costs_convex_combination(self, xn:dict, yn:dict):
        integral_costs = {}
        w = sp.symbols('w', real=True, positive=True)  # integration dummy variable
        alpha = sp.symbols("alpha", real=True)
        for u, v in self.graph.edges():
            t_uv = self.graph.edges[u, v]['travel_time']
            x_uv = self.graph.edges[u, v]['var']
            
            t_uv_w = t_uv.subs(x_uv, w)
            integral_expr = sp.integrate(t_uv_w, (w, 0, xn[x_uv] + alpha*(yn[x_uv]-xn[x_uv])))
            self.graph.edges[u, v]["integral_expr"] = integral_expr
        return alpha
    
    def _check_convergence(self, xn, xnn):
        MSE = 0
        for f, flow in xn.items():
            MSE += (flow - xnn[f])**2
        if MSE < self.error:
            return True
        else:
            return False
        
    def _make_x_from_f(self, f:dict) -> dict:
        x = {}
        for u, v in self.graph.edges():
            x[self.graph.edges[u, v]["var"]] = sum(self.graph.edges[u, v]["flows"])
            x[self.graph.edges[u, v]["var"]] = x[self.graph.edges[u, v]["var"]].subs(f)
        return x

    def _update_travel_time(self, solution, print_=True):
        for u, v in self.graph.edges():
            travel_time = self.graph.edges[u, v]["travel_time"].subs(solution)
            self.graph.edges[u, v]["flow_value"] = solution[self.graph.edges[u, v]["var"]]
            self.graph.edges[u, v]["travel_time_value"] = travel_time

    def _find_each_path(self, print_=True):
        convex_solution = {}
        for (o, d, k), (f, path) in self.f_vars.items():
            if (o, d) not in convex_solution.keys():
                convex_solution[(o, d)] = {}
            s = 0
            for i in range(len(path)-1):
                s += self.graph.edges[path[i], path[i+1]]["travel_time_value"]
            if print_:
                print(f"[Result] For flow {f} which has the following path, we have a total travel time of {s}")
                print(f"[Continue] {path}")
            convex_solution[(o, d)][f] = s
        return convex_solution
    
    def get_link_flows_travel_time2(self, solution):
        for u, v in self.graph.edges():
            travel_time = self.graph.edges[u, v]["travel_time"].subs(solution)
            self.graph.edges[u, v]["flow_value"] = solution[self.graph.edges[u, v]["var"]]
            self.graph.edges[u, v]["travel_time_value"] = travel_time
            print(f"[Result] {self.graph.edges[u, v]["var"]} => x={self.graph.edges[u, v]["flow_value"]:.1f}  --  t={travel_time:.1f}")
