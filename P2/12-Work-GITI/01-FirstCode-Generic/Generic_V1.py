from copy import deepcopy
import pandas as pd

def dataloader(data_ad):
    data = pd.read_csv(data_ad)
    data = data.iloc[13:, 1:-1]
    data.columns = ["Station", "Offset", "Elevation"]
    out_of_range = data[data["Station"] == "Out of range"].index
    data.drop(out_of_range, inplace=True)
    data.dropna(inplace=True)
    data["Station_new"] = data["Station"].apply(lambda x: float("".join(str(x).split("+"))))
    data["Offset_new"] = data["Offset"].apply(lambda x: float(str(x)[:-1]))
    data["Elevation_new"] = data["Elevation"].apply(lambda x: float("".join(str(x)[:-1].split(","))))
    data = data.sort_values(by="Station_new")
    data = data.iloc[:, -3:]
    data.columns = ["Station", "Offset", "Elevation"]
    data.index = range(len(data.index))
    return data, out_of_range

def make_class(input_data: pd.DataFrame, station_i: int, tolerance:list) -> list:
    s = []
    not_ok = 0
    find = False
    start_temp = station_i-100
    end_temp = station_i+100
    start_temp = start_temp if start_temp>100 else 0
    end_temp = end_temp if end_temp<len(input_data["Station"])-100 else len(input_data["Station"])
    for j in range(start_temp, end_temp):
        temp = input_data["Station"][j] - input_data["Station"][station_i]
        if temp >= 0  and temp <= tolerance[0]:
            s.append(j)
            not_ok = 0
            find = True
        elif temp <= 0 and temp >= -tolerance[1]:
            s.append(j)
            not_ok = 0
            find = True
        else:
            not_ok += 1
        
        if not_ok == 1 and find == True:
            break
    s.append(str(station_i)+"-id")
    return s

def add_between(data, ind, data_ind, remove_original=False, by_id=False):
    if by_id:
        ind = ind-data[0]
    first = data[:ind+1]
    last = data[ind+1:]
    first.append(data_ind)
    total = first+last
    if remove_original:
        total.pop(ind)
    return total

def sortit(classes):
    unique_tuples = {tuple(sublist) for sublist in classes}
    unique_list_of_lists = [list(t) for t in unique_tuples]
    new_unique = sorted(unique_list_of_lists, key= lambda x: x[0])
    return new_unique


def tolerance_prepare(i, stations, dev=1):
    if i == 0: 
        tolerance = ((stations[i+1][1] - stations[i][1])/dev, stations[i][1]/dev)
    elif i == len(stations)-1:
        tolerance = (stations[i][1]/dev, (stations[i][1] - stations[i-1][1])/dev)
    else:
        tolerance = ((stations[i+1][1] - stations[i][1])/dev, (stations[i][1] - stations[i-1][1])/dev)
    return tolerance

def special_sort(input_data, station_offset_allowable, number_of_each_station):
    classes = []
    stations = []

    for i in range(len(input_data["Station"])):
        print(abs(input_data["Offset"][i]), station_offset_allowable)
        if abs(input_data["Offset"][i]) <= station_offset_allowable:
            print(abs(input_data["Offset"][i]), station_offset_allowable)
            stations.append([i, input_data["Station"][i], input_data["Offset"][i]])

    for i in range(len(stations)):
        tolerance = tolerance_prepare(i, stations)
        s_class = make_class(input_data, stations[i][0], tolerance)
        classes.append(s_class)

    # need_check = True
    # dev = 1
    # while need_check:
    #     dev += 1
    #     need_check = False
    #     classes_copy = deepcopy(classes)
    #     station_copy = deepcopy(stations)
    #     for station_i in range(len(station_copy)):
    #         print(station_i)
    #         if len(classes_copy[station_i]) > number_of_each_station:
    #             # print(classes[station_i])
    #             start_temp, end_temp = classes_copy[station_i][0], classes_copy[station_i][-2]+1 # the last number is station_id
    #             for i in range(start_temp, end_temp):
    #                 if abs(input_data["Offset"][i]) <= station_offset_allowable*1:
    #                     stations = add_between(stations, station_i, [i, input_data["Station"][i], input_data["Offset"][i]])
    #                     tolerance = tolerance_prepare(station_i+1, stations, dev=1)
    #                     s_class = make_class(input_data, stations[station_i+1][0], tolerance)
    #                     # print(s_class)
    #                     classes = add_between(classes, station_i, s_class)
    #             classes.pop(station_i)
    #             stations.pop(station_i)
    #             need_check = True
    classes = sortit(classes)

    return classes

def correct_offset(input_data, data, station_id):
    station_metric = input_data["Station"][station_id]
    if station_metric%10 == 0:
        pass
    elif int(station_metric%10) <= 1:
        station_metric = int(str(station_metric)[:-3]) 
    if int(station_metric%10) >= 9:
        station_metric = int(str(station_metric)[:-3])+1
    station_new = [station_metric for _ in range(len(data))]
    offset = list(input_data.loc[data]["Offset"])
    offset = add_between(offset, station_id-data[0], 0, remove_original=True)
    elevation = input_data.loc[data]["Elevation"]
    merged_data = list(zip(station_new, data, offset, elevation))
    return sorted(merged_data, key= lambda x: x[2])

def final_preparation(final_classes):
    final_result = []
    for list_ in final_classes:
        final_result.append(["chainage", list_[0][0]])
        for item in list_:
            final_result.append([item[2], item[3]])

    result = pd.DataFrame(final_result)
    return result

def export_data(ad1, ad2, ad3, result, out_of_range_index):
    result.to_csv(ad1, index=False, header=False)
    with open(ad2, "w") as file:
        for index, row in result.iterrows():
            file.write(f"{row[0]}\t{row[1]}\n")

    with open(ad3, "w") as file:
        for row in out_of_range_index:
            file.write(f"{row}\n")

def main(ad, station_offset_allowable, max_number_of_each):
    prepared_data, out_of_range_index = dataloader(ad)
    classes = special_sort(prepared_data, station_offset_allowable, max_number_of_each)
    corrected_classes = []
    for i in range(len(classes)):
        item = correct_offset(prepared_data, classes[i][:-1], int(classes[i][-1][:-3]))
        corrected_classes.append(item)
    result = final_preparation(corrected_classes)
    return result, out_of_range_index


address = "P2/12-Work-GITI/01-FirstCode-Generic/D10 points.csv"
address_result_txt = "P2/12-Work-GITI/01-FirstCode-Generic/result.txt"
address_result_excel = "P2/12-Work-GITI/01-FirstCode-Generic/result.csv"
out_of_range_txt = "P2/12-Work-GITI/01-FirstCode-Generic/out_of_ranges.txt"

station_offset_allowable = 1  # min offset that is assume to be zero.
max_number_of_each = 30  # how many nodes can be in one class at max

result, out_of_range_index = main(address, station_offset_allowable, max_number_of_each)
export_data(address_result_excel, address_result_txt, out_of_range_txt, result, out_of_range_index)

