import pandas as pd
import random

num_rows = 1000

data = []
for player_id in range(num_rows):
    arrival_time = random.randint(0, 3599)
    source = random.randint(1, 24)
    destination = random.randint(1, 24)
    while destination == source:
        destination = random.randint(1, 24)
    data.append({
        "player_id": player_id,
        "arrival_time": arrival_time,
        "source": source,
        "destination": destination
    })

df = pd.DataFrame(data)
df.sort_values(by=["arrival_time"], inplace=True, ignore_index=True)
df["player_id"] = df.index
df.to_csv("/mnt/Data1/Python_Projects/Pure-Python/P5/08-Advanced_Traffic_TA_Class/data/network/demand.csv", index=False)