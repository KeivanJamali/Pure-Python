import pandas as pd


def bracket_duration(data):
    treshold = 0.05
    data_ = data.loc[:, ["Time [sec]", "Acceleration [g]"]]
    data_.loc[:, "abs_A"] = abs(data_.loc[:, "Acceleration [g]"])
    for i in range(len(data_)):
        if data_.iloc[i, 2] > treshold:
            start_time = data_.iloc[i, 0]
            break
    for i in range(len(data_) - 1, -1, -1):
        if data_.iloc[i, 2] > treshold:
            end_time = data_.iloc[i, 0]
            break
    print(f"duration of the earthquake is {end_time - start_time}")


def significant_duration(data, name1, name2):
    treshold = 0.05
    data_ = data.loc[:, [f"{name1}", f"{name2}"]]
    for i in range(len(data_)):
        if data_.iloc[i, 1] > treshold:
            start_time = data_.iloc[i, 0]
            break
    for i in range(len(data_) - 1, -1, -1):
        if data_.iloc[i, 1] > treshold:
            end_time = data_.iloc[i, 0]
            break
    print(end_time, start_time)
    print(f"duration of the earthquake is {end_time - start_time}")
