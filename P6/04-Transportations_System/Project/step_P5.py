from modular.extract_network import Graph
from modular.ConvexCombination import ConvexCombination
from student_info import students
from pathlib import Path
import hashlib

def solve_p5(student_id, student_name, OD_percent_list, cap_percent_list, tol=1e-4, max_iterations=2000):
    models = {}
    save_path = Path(f"/Users/keivanjamali/Projects/Pure-Python/P6/04-Transportations_System/Project/ConvexCombination_Res")
    network = Graph()
    seed = int(hashlib.sha256(student_id.encode()).hexdigest(), 16) % int(1e8)
    network.add_free_flow_speed(seed)
    network.add_capacity(seed)
    network.add_OD_demand(seed)
    network.add_zero_flow()
    model = ConvexCombination(network)
    model.run(max_iterations=max_iterations, tol=tol, log=False)
    model.plot_history(start_iteration=100, save_path=save_path/f"{student_name}_main.png")
    models["main"] = model

    for od_percent in OD_percent_list:
        network = Graph()
        seed = int(hashlib.sha256(student_id.encode()).hexdigest(), 16) % int(1e8)
        network.add_free_flow_speed(seed)
        network.add_capacity(seed)
        network.add_OD_demand(seed)
        network.add_percent_to_OD(od_percent)
        network.add_zero_flow()
        model = ConvexCombination(network)
        model.run(max_iterations=max_iterations, tol=tol, log=False)
        model.plot_history(start_iteration=100, save_path=save_path/f"{student_name}_OD{int(od_percent*100)}.png")
        models[f"OD{int(od_percent*100)}"] = model

    for cap_percent in cap_percent_list:
        network = Graph()
        seed = int(hashlib.sha256(student_id.encode()).hexdigest(), 16) % int(1e8)
        network.add_free_flow_speed(seed)
        network.add_capacity(seed)
        network.add_OD_demand(seed)
        network.reduce_capacity_by_percent(cap_percent)
        network.add_zero_flow()
        model = ConvexCombination(network)
        model.run(max_iterations=max_iterations, tol=tol, log=False)
        model.plot_history(start_iteration=100, save_path=save_path/f"{student_name}_CAP{int(cap_percent*100)}.png")
        models[f"CAP{int(cap_percent*100)}"] = model
        
    return models


    
if __name__ == "__main__":
    for student_name, student_id in students.items():
        od_list = [0.1, 0.25, 0.5]
        cap_list = [0.1, 0.25, 0.5]
        solve_p5(student_id, student_name, od_list, cap_list)
    # od_list = [0.1, 0.25, 0.5]
    # cap_list = [0.1, 0.25, 0.5]
    # solve_p5("403209743", "KeivanJamali", od_list, cap_list)

