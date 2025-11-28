import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# --- Load your files ---
path_nodes = "SiouxFallsxy.csv"
path_links = "SiouxFallsNetwork.csv"
nodes = pd.read_csv(path_nodes, index_col=0)
links = pd.read_csv(path_links)

# --- Helper functions ---
def compute_length(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def get_speed():
    return 80  # km/h

def compute_travel_time(length, speed_kmph):
    speed_mps = speed_kmph * 1000 / 3600
    return length / speed_mps

# --- Main graph builder ---
def make_graph(nodes, links):
    G = nx.DiGraph()

    # --- Add nodes with attributes ---
    for _, row in nodes.iterrows():
        node_id, x, y = row

        G.add_node(node_id,
                   pos=(x, y),
                   capacity=0,
                   type=None,
                   entry_rate=0,
                   exit_rate=0,
                   traffic_signal=False,
                   priority=None,
                   signal_cycle=0,
                   congestion_level=None,
                   sensor=False,
                   queue_length=0)  # NEW: queue length at intersection

    # --- Add edges with computed and default attributes ---
    for _, row in links.iterrows():
        start = int(row["from"])
        end = int(row["to"])
        #G.nodes[start] -> returns a dictionary of attributes
        #G.nodes[start]["pos"] -> This extracts the position attribute of the node — a tuple (x, y) representing its coordinates.
        pos_start = G.nodes[start]["pos"]
        pos_end = G.nodes[end]["pos"]

        length = compute_length(pos_start, pos_end)
        speed = get_speed()
        travel_time = compute_travel_time(length, speed)

        block_count = int(length // 100)
        block_capacity = 20

        G.add_edge(start, end,
                   length=length,
                   lanes=0,
                   speed=speed,
                   travel_time=travel_time,
                   capacity=0,
                   type=None,
                   flow=0,
                   is_blocked=False,
                   accident_risk=None,
                   toll=False,
                   direction=None,
                   split_ratio=0,
                   block_count=block_count,
                   block_capacity=block_capacity)

    return G

# --- Vehicle list with attributes --- -> list of dictionaries
vehicles = []

# Example: add one vehicle manually (later this will be dynamic)
vehicles.append({
    "id": 1,
    "entry_time": None,              # time vehicle enters the network
    "current_edge": None,            # current edge
    "current_block": None,           # current block number
    "delay_time": 0,                 # total delay accumulated
    "path": []          
})

# --- Build and draw the network ---
G = make_graph(nodes, links)
pos = nx.get_node_attributes(G, "pos") # this line extracts the "pos" attribute from all nodes in the graph
nx.draw(G, with_labels=True, pos=pos)  # with_labels=True: shows node IDs as labels
plt.show()