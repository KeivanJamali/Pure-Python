from modular.extract_network import Graph
from modular.simple_assignments import engine
from pathlib import Path

result_path_1 = Path(r"/Users/keivanjamali/Downloads/P1&P2-Shokouhikia_404300874/output_n20.txt")
result_path_2 = Path(r"/Users/keivanjamali/Downloads/P1&P2-Shokouhikia_404300874/output-10%.txt")
correct_path_default = Path(r"/Users/keivanjamali/Projects/Pure-Python/P6/04-Transportations_System/Project/test.txt")
st_number = "404300874"

def compare_files(path1: Path, path2: Path):
    with open(path1, "r") as f:
        data_main = f.readlines()
    with open(path2, "r") as f:
        data_secondary = f.readlines()    
    assert len(data_main) == len(data_secondary)
    
    counts = 0
    error = 0
    for i in range(len(data_secondary)):
        s = data_secondary[i].strip().split(", ")
        for j in range(len(data_main)):
            m = data_main[j].strip().split(", ")
            if int(s[0]) == int(m[0]) and int(s[1]) == int(m[1]):
                counts += 1
                error += abs(float(s[2]) - float(m[2]))
                break
    return counts, error
                
network = Graph()
algorithm = engine(graph=network, student_id=st_number, init_flow=0, init_capacity=1000)
algorithm.run_incremental_fixed(fixed_n=20)
algorithm.get_result_as_file(correct_path_default)
t = algorithm.get_total_flow()
c, e = compare_files(correct_path_default, result_path_1)
print(f"First Part error: {e} which is {e/t*100:.2f}%.")

network = Graph()
algorithm = engine(graph=network, student_id=st_number, init_flow=0, init_capacity=1000)
algorithm.run_incremental_percentage(percentage=0.1, threshold=1e-6)
algorithm.get_result_as_file(correct_path_default)
t = algorithm.get_total_flow()
c, e = compare_files(correct_path_default, result_path_2)
print(f"Second Part error: {e} which is {e/t*100:.2f}%.")
