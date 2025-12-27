import random
import pandas as pd
from pathlib import Path

def generate_demand(network_file_path: Path, demand_file_path: Path,
                    amount: int, time: int):
    network = pd.read_csv(network_file_path)
    # Get all unique nodes in the network
    all_nodes = list(set(network["from"].tolist() + network["to"].tolist()))
    demand_data = pd.DataFrame(columns=["arrival_time", "source", "destination"])
    
    for _ in range(amount):
        arrival_time = random.randint(0, time)
        source, destination = random.sample(all_nodes, 2)
        
        demand_data.loc[len(demand_data)] = {
            "arrival_time": arrival_time,
            "source": source,
            "destination": destination
        }
        
    
    demand_data.sort_values(by="arrival_time", inplace=True)
    demand_data["player_id"] = range(1, len(demand_data)+1)
    demand_data.to_csv(demand_file_path, index=False)


if __name__ == "__main__":
    # network_file = Path(r"/mnt/Data1/Python_Projects/Pure-Python/P5/08-Advanced_Traffic_TA_Class/data/network/SiouxFallsNetwork.csv")
    # demand_file = Path(r"/mnt/Data1/Python_Projects/Pure-Python/P5/08-Advanced_Traffic_TA_Class/data/network/demand.csv")
    network_file = Path(r"/mnt/Data1/Python_Projects/Pure-Python/P5/08-Advanced_Traffic_TA_Class/data/network_test/SiouxFallsNetwork.csv")
    demand_file = Path(r"/mnt/Data1/Python_Projects/Pure-Python/P5/08-Advanced_Traffic_TA_Class/data/network_test/demand.csv")
    generate_demand(network_file, demand_file, amount=800, time=400)