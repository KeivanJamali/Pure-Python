from modular.extract_network import Graph
from modular.simple_assignments import engine

st_number = "404300874"
important_number = "369528"

network = Graph()
algorithm = engine(network, st_number, init_flow=0, init_capacity=1000)
algorithm.run_allornothing()
IMPORTANT_NUMBER = algorithm.get_important_number()

if int(IMPORTANT_NUMBER) == int(important_number):
    print(f"[Correct Answer] IMPORTANT NUMBER is : {IMPORTANT_NUMBER}")
else:
    print(f"[Wrong Answer] {IMPORTANT_NUMBER} is no {important_number}")
