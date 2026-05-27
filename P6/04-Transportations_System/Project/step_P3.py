from modular.optimization_algorithms import BiSection, GoldenSection
from student_info import students
import numpy as np
import hashlib

def part3_solve(student_id, log=False) -> tuple[tuple, tuple]:
    seed = int(hashlib.sha256(student_id.encode()).hexdigest(), 16)
    seed = seed % int(1e8)
    print(seed)
    B = 0.15 + (int(seed) % 10) / 100
    T0 = 5 + (int(seed) % 10)
    C = 1000
    K = T0 + (int(seed) % (T0*(1+5*B) - T0))
    def travel_time(f):
        # f = np.asarray(f)
        y = T0 * (1 + B * (f / C)**4)
        return y * f
    optim = BiSection(loss_function=travel_time, a=0, b=C, epsilon=1e-5)
    x_bi, y_bi = optim.step(epsilon=1e-5, log=log, K=K)
    if log:
        print(f"[Problem1] BiSection: x={x_bi}, y={y_bi}")
    x_bi, y_bi = round(x_bi), round(y_bi)
    print(x_bi, y_bi)
    p1 = int(hash(tuple([x_bi, y_bi])) % 100000)

    # SOLVE P2
    with open(r"/Users/keivanjamali/Projects/Pure-Python/P6/04-Transportations_System/Project/data/network_P3.txt", "r") as f:
        for line in f:
            if line.startswith(student_id):
                network_str = line.split(": ", 1)[1]
                network = eval(network_str)
                break
    def loss_function(lmbd):
        total = 0.0
        for edge in network:
            d = network[edge]
            f = d["x"] + lmbd * (d["y"] - d["x"])
            T = d["t0"] * (1 + d["B"] * (f / C) ** 4)
            total += f * T
        return total
    optim = GoldenSection(loss_function=loss_function, a=0, b=1, epsilon=1e-5)
    x_golde, y_golde = optim.step(log=True)
    if log:
        print(f"[Problem2] GoldenSection: x={x_golde}, y={y_golde}") 
    x_golde, y_golde = round(x_golde, 4), round(y_golde)
    print(x_golde, y_golde)
    p2 = int(hash(tuple([x_golde, y_golde])) % 1e5)
    return p1, p2

for st, num in students.items():
    res = part3_solve(num)
    print(st, res)