import pandas as pd

def get_panda_data(data):
    panda_data = pd.DataFrame(data.fetchall(), columns=data.keys())
    return panda_data
