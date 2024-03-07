import pandas as pd


def get_sma(data, n, detail=False):
    data_ = data.loc[:, ["Time [sec]", "Acceleration [g]", "SE_Velocity [m/sec]", "SE_Displacement [m]"]]
    data_.loc[:, "abs_A"] = abs(data_.loc[:, "Acceleration [g]"])
    data_.loc[:, "abs_V"] = abs(data_.loc[:, "SE_Velocity [m/sec]"])
    data_.loc[:, "abs_D"] = abs(data_.loc[:, "SE_Displacement [m]"])
    a_abs_max_time_data = []
    v_abs_max_time_data = []
    d_abs_max_time_data = []

    for i in range(1, len(data_) - 1):
        a_d0 = data_.iloc[i - 1, 4]
        a_d1 = data_.iloc[i, 4]
        a_d2 = data_.iloc[i + 1, 4]

        v_d0 = data_.iloc[i - 1, 5]
        v_d1 = data_.iloc[i, 5]
        v_d2 = data_.iloc[i + 1, 5]

        d_d0 = data_.iloc[i - 1, 6]
        d_d1 = data_.iloc[i, 6]
        d_d2 = data_.iloc[i + 1, 6]
        if a_d1 - a_d0 > 0 > a_d2 - a_d1:
            a_abs_max_time_data.append([data_.iloc[i, 4], data_.iloc[i, 1], data_.iloc[i, 0]])

        if v_d1 - v_d0 > 0 > v_d2 - v_d1:
            v_abs_max_time_data.append([data_.iloc[i, 5], data_.iloc[i, 2], data_.iloc[i, 0]])

        if d_d1 - d_d0 > 0 > d_d2 - d_d1:
            d_abs_max_time_data.append([data_.iloc[i, 6], data_.iloc[i, 3], data_.iloc[i, 0]])

    a_sorted_max = sorted(a_abs_max_time_data, key=lambda x: x[0], reverse=True)
    v_sorted_max = sorted(v_abs_max_time_data, key=lambda x: x[0], reverse=True)
    d_sorted_max = sorted(d_abs_max_time_data, key=lambda x: x[0], reverse=True)

    print(
        f"[ANSWER] Maximum Acceleration: {a_sorted_max[n - 1][1]} g,At time {a_sorted_max[n - 1][2]} sec.")
    if detail:
        print(
            f"[ANSWER] Maximum Velocity: {v_sorted_max[n - 1][1]} m/sec,At time {v_sorted_max[n - 1][2]} sec.")
        print(
            f"[ANSWER] Maximum Displacement: {d_sorted_max[n - 1][1]} m,At time {d_sorted_max[n - 1][2]} sec.")
