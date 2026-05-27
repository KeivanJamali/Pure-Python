from modular.travel_time_generator import travel_time_calculator
from modular.optimization_algorithms import GoldenSection

import networkx as nx
import matplotlib.pyplot as plt

class ConvexCombination:
    def __init__(self, network):
        self.history = {}
        self.network = network
        self.update_travel_times()
        self.zero_auxiliary_flows()
        for o in self.network.graph.nodes():
            self.assign_auxiliary_by_origin(o)
        self.update_flows(alpha=1.0)
        self.history_objective_value_temp = 0
        self.alpha_temp = 1
        self.relative_gap = float('inf')
        self.update_history(iteration=0)
        
    def update_travel_times(self):
        for u, v in self.network.graph.edges:
            capacity = self.network.graph[u][v]["capacity"]
            flow = self.network.graph[u][v]["flow"]
            free_flow_travel_time = self.network.graph[u][v]["free_flow_travel_time"]
            self.network.graph[u][v]["travel_time"] = travel_time_calculator(capacity=capacity, 
                                                                             flow=flow, 
                                                                             free_flow_travel_time=free_flow_travel_time)
            
    def shortest_path_single_to_all(self, o):
        paths = nx.single_source_all_shortest_paths(self.network.graph,
                                                    o, weight="travel_time")
        if paths:
            return dict(paths)
        else:
            None
            
    def zero_auxiliary_flows(self):
        for u, v in self.network.graph.edges:
            self.network.graph[u][v]["y"] = 0
            
    def assign_auxiliary_by_origin(self, o):
        paths = self.shortest_path_single_to_all(o)
        if paths:
            for j in self.network.graph.nodes():
                if j != o:
                    if j in paths.keys():
                        selected_path = sorted(paths[j])[0]
                        for z in range(len(selected_path)-1):
                            self.network.graph[selected_path[z]][selected_path[z+1]]["y"] += self.network.graph.nodes[o]["OD_demand"][j]
                            
    def line_search(self, tol=1e-8):
        def objective_function(alpha):
            total_loss = 0
            for u, v in self.network.graph.edges:
                c = self.network.graph[u][v]["capacity"]
                t0 = self.network.graph[u][v]["free_flow_travel_time"]
                x = self.network.graph[u][v]["flow"]
                y = self.network.graph[u][v]["y"]
                flow = x + alpha * (y - x)
                
                # # Integral of the travel time function from 0 to flow.
                # for i in range(1, int(flow)+1):
                #     total_loss += travel_time_calculator(capacity, i, free_flow_travel_time)
                # closed_form integral of the BPR function: t0 * (flow + (0.15 * c / (4 + 1)) * (flow / c) ** (4 + 1))
                total_loss += t0 * (flow + (0.15 * c / (4 + 1)) * (flow / c) ** (4 + 1))
            return total_loss
        
        optim = GoldenSection(objective_function, 0, 1, epsilon=tol)
        x_golde, y_golde = optim.step(log=False)
        self.history_objective_value_temp = y_golde
        self.alpha_temp = x_golde
        return self.alpha_temp
    
    def update_flows(self, alpha):
        for u, v in self.network.graph.edges:
            x = self.network.graph[u][v]["flow"]
            y = self.network.graph[u][v]["y"]
            new_flow = x + alpha * (y - x)
            self.network.graph[u][v]["previous_flow"] = x
            self.network.graph[u][v]["flow"] = new_flow
            
    def update_history(self, iteration):
        total_travel_time = 0
        for u, v in self.network.graph.edges:
            flow = self.network.graph[u][v]["flow"]
            travel_time = self.network.graph[u][v]["travel_time"]
            total_travel_time += flow * travel_time
        self.history[iteration] = {"total_travel_time": total_travel_time/len(self.network.graph.edges),
                                   "objective_value": self.history_objective_value_temp,
                                   "step_size": self.alpha_temp,
                                   "relative_gap": self.relative_gap}
            
    def check_convergence(self, tol=1e-6):
        numerator = 0
        denominator = 0
        for u, v in self.network.graph.edges:
            x = self.network.graph[u][v]["flow"]
            y = self.network.graph[u][v]["previous_flow"]
            numerator += abs(y - x)
            denominator += abs(x)
        self.relative_gap = numerator / max(denominator, 1e-12)
        return self.relative_gap < tol
    
    def step(self, iteration, tol, log=True):
        self.zero_auxiliary_flows()
        for o in self.network.graph.nodes():
            self.assign_auxiliary_by_origin(o)
        check = self.check_convergence(tol)
        alpha = self.line_search(tol=1e-8)
        self.update_flows(alpha)
        self.update_travel_times()
        self.update_history(iteration)
        if log:
            print(f"Iteration {iteration}: Gap = {self.relative_gap:.6f}, Step Size (alpha) = {alpha:.4f}")
        return check
        
    def run(self, max_iterations=1000, tol=1e-6, log=False):
        for iteration in range(1, max_iterations+1):
            check = self.step(iteration, tol, log)
            if check and iteration > 10:
                print(f"Convergence achieved at iteration {iteration}.")
                break
            
    def plot_objective_history(self):
        iterations = list(self.history.keys())
        objective_values = [self.history[i]["objective_value"] for i in iterations]
        plt.plot(iterations, objective_values, marker='o')
        plt.xlabel("Iteration")
        plt.ylabel("Objective Value")
        plt.title("Objective Value History")
        plt.grid()
        plt.show()
    
    def plot_step_size_history(self):
        iterations = list(self.history.keys())
        step_sizes = [self.history[i]["step_size"] for i in iterations]
        plt.plot(iterations, step_sizes, marker='o')
        plt.xlabel("Iteration")
        plt.ylabel("Step Size (alpha)")
        plt.title("Step Size History")
        plt.grid()
        plt.show()
        
    def plot_total_travel_time_history(self):
        iterations = list(self.history.keys())
        total_travel_times = [self.history[i]["total_travel_time"] for i in iterations]
        plt.plot(iterations, total_travel_times, marker='o')
        plt.xlabel("Iteration")
        plt.ylabel("Total Travel Time")
        plt.title("Total Travel Time History")
        plt.grid()
        plt.show()
        
    def plot_relative_gap_history(self):
        iterations = list(self.history.keys())
        relative_gaps = [self.history[i]["relative_gap"] for i in iterations]
        plt.plot(iterations, relative_gaps, marker='o')
        plt.xlabel("Iteration")
        plt.ylabel("Relative Gap")
        plt.title("Relative Gap History")
        plt.grid()
        plt.show()

    def plot_history(self, start_iteration=1, end_iteration=None, save_path=None):
        fig, axes = plt.subplots(1, 4, figsize=(20, 5))
        iterations = list(self.history.keys())
        iterations = [i for i in iterations if (i >= start_iteration and (end_iteration is None or i <= end_iteration))]
        objective_values = [self.history[i]["objective_value"] for i in iterations]
        step_sizes = [self.history[i]["step_size"] for i in iterations]
        total_travel_times = [self.history[i]["total_travel_time"] for i in iterations]
        relative_gaps = [self.history[i]["relative_gap"] for i in iterations]
        axes[0].plot(iterations, objective_values, marker='o')
        axes[0].set_xlabel("Iteration")
        axes[0].set_ylabel("Objective Value")
        axes[0].set_title("Objective Value History")
        axes[0].grid()
        axes[1].plot(iterations, step_sizes, marker='o')
        axes[1].set_xlabel("Iteration")
        axes[1].set_ylabel("Step Size (alpha)")
        axes[1].set_title("Step Size History")
        axes[1].grid()
        axes[2].plot(iterations, total_travel_times, marker='o')
        axes[2].set_xlabel("Iteration")
        axes[2].set_ylabel("Total Travel Time")
        axes[2].set_title("Total Travel Time History")
        axes[2].grid()
        axes[3].plot(iterations, relative_gaps, marker='o')
        axes[3].set_xlabel("Iteration")
        axes[3].set_ylabel("Relative Gap")
        axes[3].set_title("Relative Gap History")
        axes[3].grid()
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
    