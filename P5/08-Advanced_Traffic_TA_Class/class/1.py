import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

NETWORK_FILE = r"/mnt/Data1/Python_Projects/Pure-Python/P5/08-Advanced_Traffic_TA_Class/data/network/SiouxFallsNetwork.csv"
NODE_FILE = r"/mnt/Data1/Python_Projects/Pure-Python/P5/08-Advanced_Traffic_TA_Class/data/network/SiouxFallsXY.csv"
OUTPUT_DIR = "Output_P4"

TIME_STEP_S = 1.0
CYCLE_TIME_S = 60.0
VEH_SPEED_KMH = 80.0

OD_LIST = [
    (10, 16), (2, 19), (3, 18), (4, 17), (5, 16),
    (6, 15), (7, 14), (8, 13), (9, 24), (10, 23),
]

VEH_SPEED_MPS = VEH_SPEED_KMH * 1000 / 3600  # m/s


class Vehicle:
    def __init__(self, vid, node_path, network):
        self.id = vid
        self.path = node_path
        self.index = 0
        self.current_node = node_path[0]
        self.finished = False
        self.travel_time = 0.0
        self.time_on_link = 0.0
        self.network = network
        self.set_time_on_link()

    def set_time_on_link(self):
        nxt = self.next_node()
        if nxt is not None:
            length = self.network.G[self.current_node][nxt]['weight']
            self.time_on_link = length / VEH_SPEED_MPS
        else:
            self.time_on_link = 0.0

    def next_node(self):
        if self.index + 1 < len(self.path):
            return self.path[self.index + 1]
        return None

    def step(self, dt):
        if self.finished:
            return
        self.travel_time += dt
        if self.time_on_link > 0:
            self.time_on_link -= dt

    def can_move(self):
        nxt = self.next_node()
        if nxt is None:
            return False
        inter = self.network.intersections[nxt]
        u = self.current_node
        return self.time_on_link <= 0 and inter.is_green(u)

    def move_to_next(self):
        nxt = self.next_node()
        if nxt is None:
            self.finished = True
            return
        self.index += 1
        self.current_node = nxt
        if self.index == len(self.path) - 1:
            self.finished = True
            self.time_on_link = 0.0
        else:
            self.set_time_on_link()


class Intersection:
    def __init__(self, node_id):
        self.id = node_id
        self.time = 0.0
        self.incoming = []

    def add_incoming(self, u):
        if u not in self.incoming:
            self.incoming.append(u)

    def step(self, dt):
        self.time = (self.time + dt) % CYCLE_TIME_S

    def is_green(self, u):
        if not self.incoming:
            return True
        phase_len = CYCLE_TIME_S / len(self.incoming)
        k = int(self.time // phase_len)
        k = min(k, len(self.incoming) - 1)
        return self.incoming[k] == u


class Stats:
    def __init__(self):
        self.trajectories = []
        self.summary = []

    def record_step(self, t, v):
        self.trajectories.append({
            "time_s": t,
            "vehicle_id": v.id,
            "node": v.current_node,
            "finished": v.finished,
            "travel_time_s": v.travel_time,
        })

    def record_summary(self, v):
        self.summary.append({
            "vehicle_id": v.id,
            "origin": v.path[0],
            "destination": v.path[-1],
            "travel_time_s": v.travel_time,
        })

    def export(self, folder):
        os.makedirs(folder, exist_ok=True)
        pd.DataFrame(self.trajectories).to_csv(os.path.join(folder, "p4_trajectories.csv"), index=False)
        pd.DataFrame(self.summary).to_csv(os.path.join(folder, "p4_summary.csv"), index=False)


class TrafficNetwork:
    def __init__(self, net_file, node_file):
        self.net_file = net_file
        self.node_file = node_file
        self.G = nx.DiGraph()
        self.intersections = {}

    def build(self):
        nodes = pd.read_csv(self.node_file)
        for _, row in nodes.iterrows():
            nid = int(row["node"])
            x = float(row["x"])
            y = float(row["y"])

            self.G.add_node(nid, pos=(x, y))
            self.intersections[nid] = Intersection(nid)

        # خواندن یال‌ها
        links = pd.read_csv(self.net_file)
        for _, row in links.iterrows():
            u = int(row["from"])
            v = int(row["to"])
            length = float(row["length"])
            self.G.add_edge(u, v, weight=length)
            self.intersections[v].add_incoming(u)

    def shortest_path(self, o, d):
        try:
            return nx.shortest_path(self.G, o, d, weight="weight")
        except nx.NetworkXNoPath:
            return None

    def plot_network(self):
        pos = nx.get_node_attributes(self.G, 'pos')

        G_undirected = self.G.to_undirected()

        plt.figure(figsize=(12, 12))

        nx.draw_networkx_nodes(self.G, pos, node_size=700, node_color='lightgreen', edgecolors='black', linewidths=1.5)

        nx.draw_networkx_labels(self.G, pos, font_size=10, font_weight='bold')

        nx.draw_networkx_edges(
            self.G,
            pos,
            edge_color='gray',
            arrows=True,
            arrowsize=20,
            width=2,
            arrowstyle='-|>',
            connectionstyle='arc3, rad=0.0'
        )

        edge_labels = nx.get_edge_attributes(G_undirected, 'weight')
        formatted_edge_labels = {k: f"{int(v)}" for k, v in edge_labels.items()}

        nx.draw_networkx_edge_labels(
            G_undirected,
            pos,
            edge_labels=formatted_edge_labels,
            font_size=9,
            label_pos=0.5,
            font_color='black',
            font_weight='bold',
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=0.5)
        )

        plt.title("Sioux Falls Network (Bidirectional Visualization)")
        plt.axis('off')
        plt.tight_layout()
        plt.show()
class Simulation:
    def __init__(self, network, dt):
        self.net = network
        self.dt = dt
        self.time = 0.0
        self.vehicles = []
        self.stats = Stats()

    def add_vehicle(self, v):
        self.vehicles.append(v)
        self.stats.record_step(self.time, v)

    def all_finished(self):
        return len(self.vehicles) > 0 and all(v.finished for v in self.vehicles)

    def step_signals(self):
        for inter in self.net.intersections.values():
            inter.step(self.dt)

    def step_vehicles(self):
        for v in self.vehicles:
            if v.finished:
                self.stats.record_step(self.time, v)
                continue
            v.step(self.dt)
            if v.can_move():
                v.move_to_next()
            self.stats.record_step(self.time, v)

    def run(self, max_steps=100000):
        steps = 0
        while not self.all_finished() and steps < max_steps:
            self.step_signals()
            self.step_vehicles()
            self.time += self.dt
            steps += 1
        for v in self.vehicles:
            self.stats.record_summary(v)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    net = TrafficNetwork(NETWORK_FILE, NODE_FILE)
    net.build()

    print("Displaying network graph...")
    net.plot_network()

    sim = Simulation(net, TIME_STEP_S)

    vid = 1
    for o, d in OD_LIST:
        if o == d:
            continue
        path = net.shortest_path(o, d)
        if path is None:
            continue
        v = Vehicle(vid, path, net)
        sim.add_vehicle(v)
        vid += 1

    sim.run()
    sim.stats.export(OUTPUT_DIR)
    print("Part 4 finished. Results in", OUTPUT_DIR)


if __name__ == "__main__":
    main()