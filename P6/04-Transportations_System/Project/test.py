import pandas as pd
import networkx as nx
import hashlib

student_id = "403206113"
network_file = "/Users/keivanjamali/Projects/Pure-Python/P6/04-Transportations_System/Project/data/SiouxFallsNetwork.csv"
xy_file = "/Users/keivanjamali/Projects/Pure-Python/P6/04-Transportations_System/Project/data/SiouxFallsXY.csv"
out1_file = "/Users/keivanjamali/Projects/Pure-Python/P6/04-Transportations_System/Project/o1.txt"
out2_file = "/Users/keivanjamali/Projects/Pure-Python/P6/04-Transportations_System/Project/o2.txt"
capacity = 1000.0
tol = 0.000001


def sha3_int(text):
    return int(hashlib.sha3_256(text.encode("utf-8")).hexdigest(), 16)


def get_A_B(student_id):
    seed = sha3_int(str(student_id))
    A = (seed % 100) / 100.0 + 1.0
    B = (seed % 50) / 100.0 + 0.5
    return A, B


def build_od(nodes, student_id):
    od = {}
    for o in nodes:
        for d in nodes:
            if o != d:
                od_seed = sha3_int(str(student_id) + str(o) + str(d))
                od[(o, d)] = (od_seed % 100) + 10
    return od


def build_graph(df, A, B):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        i = int(row["from"])
        j = int(row["to"])
        L = float(row["length"])
        t0 = A * L
        G.add_edge(i, j, length=L, t0=t0, B=B, capacity=capacity, flow=0.0, time=t0)
    return G


def update_times(G):
    for u, v, data in G.edges(data=True):
        f = data["flow"]
        t0 = data["t0"]
        B = data["B"]
        c = data["capacity"]
        data["time"] = t0 * (1 + B * (f / c) ** 4)


def shortest_path_with_tie_break(G, o, d):
    paths = list(nx.all_shortest_paths(G, o, d, weight="time"))
    return min(paths, key=lambda p: tuple(p))


def assign_flow(G, path, q):
    for u, v in zip(path[:-1], path[1:]):
        G[u][v]["flow"] += q


def save_flows(G, filename):
    lines = []
    for u, v in sorted(G.edges()):
        f = round(G[u][v]["flow"], 1)
        lines.append(f"{u}, {v}, {f}")
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def run_output1(G, od):
    for _ in range(20):
        update_times(G)
        for (o, d), q in od.items():
            part = 0.05 * q
            path = shortest_path_with_tie_break(G, o, d)
            assign_flow(G, path, part)
    return G


def run_output2(G, od, tol=0.001, max_iter=10000):
    prev_part = None
    k = 1
    while k <= max_iter:
        alpha = 0.1 * (0.9 ** (k - 1))

        if prev_part is not None:
            diff = max(abs(q * alpha - q * prev_part) for q in od.values())
            if diff < tol:
                break

        update_times(G)

        for (o, d), q in od.items():
            part = q * alpha
            path = shortest_path_with_tie_break(G, o, d)
            assign_flow(G, path, part)

        prev_part = alpha
        k += 1

    return G, k - 1


def main():
    net = pd.read_csv(network_file)
    xy = pd.read_csv(xy_file)

    nodes = sorted(xy["node"].astype(int).tolist())
    A, B = get_A_B(student_id)
    od = build_od(nodes, student_id)

    G1 = build_graph(net, A, B)
    G1 = run_output1(G1, od)
    save_flows(G1, out1_file)

    G2 = build_graph(net, A, B)
    G2, n_iter = run_output2(G2, od, tol)
    save_flows(G2, out2_file)


if __name__ == "__main__":
    main()