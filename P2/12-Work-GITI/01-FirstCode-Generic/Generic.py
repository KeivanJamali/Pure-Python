import pandas as pd

def prepare_data(data):
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

def special_sort(input_data, initial_point, final_point, space, tolerance):
    n = int(((final_point - initial_point)/space)+1)
    classes = []
    init_s = initial_point

    for _ in range(n):
        s = []
        not_ok = 0
        find = False
        for i in range(len(input_data["Station"])):
            if abs(input_data["Station"][i] - init_s) <= tolerance:
                s.append(i)
                not_ok = 0
                find = True
            else:
                not_ok += 1
            
            if not_ok == 10 and find == True:
                break
        classes.append(s)
        init_s = init_s + space

    return classes

def make_classes(data, initial_point, space, error):
    sorted_classes = []
    for c in range(len(classes)):
        station_new = [initial_point for _ in range(len(classes[c]))]
        need_sort = data.loc[classes[c]]["Offset"]
        additional = data.loc[classes[c]]["Elevation"]
        need_sort = list(zip(station_new, classes[c], need_sort, additional))
        if need_sort:
            done = False
            choices = []
            for i in range(len(need_sort)):
                if abs(need_sort[i][2]) <= error:
                    choices.append([i, need_sort[i][2], need_sort[i][3]])
                    done = True
            if done:
                temp = min(choices, key=lambda x: x[1])
                exact = (need_sort[0][0], 0, 0, temp[2])
                need_sort.pop(temp[0])
            if not done:
                for i in range(len(need_sort)):
                    o = need_sort[i][2]
                    if o > 0:
                        temp1 = float("inf")
                        if o < temp1:
                            temp1 = o
                            temp1i = i
                    elif o < 0:
                        o = -o
                        temp2 = float("inf")
                        if o < temp2:
                            temp2 = o
                            temp2i = i
                exact = (need_sort[0][0], 0, 0, (temp1*need_sort[temp1i][3] + temp2*need_sort[temp2i][3])/(temp1+temp2))
            need_sort.append(exact)
            sorted_elemnets = sorted(list(need_sort), key=lambda x: x[2])
            sorted_classes.append(sorted_elemnets)
        initial_point += space

    return sorted_classes

def final_preparation(final_classes):
    final_result = []
    for list_ in final_classes:
        final_result.append(["chainage", list_[0][0]])
        for item in list_:
            final_result.append([item[2], item[3]])

    result = pd.DataFrame(final_result)
    return result


def second_special_sort(input_data, initial_point, final_point, space, tolerance, pre_classes):
    n = int(((final_point - initial_point)/space)+1)
    classes = special_sort(input_data, initial_point, final_point, space, tolerance)
    visited_items = [item for sublist in classes for item in sublist]
    visited_items = set(visited_items)

    total_items = [item for sublist in pre_classes for item in sublist]
    total_items = set(total_items)
    diffrences = list(total_items - visited_items)
    
    result_for_station = [(i+1, input_data["Station"][i]) for i in diffrences]
    result_for_station_sorted = sorted(result_for_station, key= lambda x: x[1])

    return result_for_station_sorted

############################################################################################################

address = "P2/12-Work-GITI/01-FirstCode-Generic/D10 points.csv"
address_result_txt = "P2/12-Work-GITI/01-FirstCode-Generic/result.txt"
address_result_excel = "P2/12-Work-GITI/01-FirstCode-Generic/result.csv"
diffrences_result_txt = "P2/12-Work-GITI/01-FirstCode-Generic/diffrences_result.txt"
out_of_range_txt = "P2/12-Work-GITI/01-FirstCode-Generic/out_of_ranges.txt"
data = pd.read_csv(address)

initial_point = 3600
final_point = 20900
space_between = 20
first_tolerance = space_between/2
second_tolerance = space_between/4
error = 0.2

############################################################################################################

prepared_data, out_of_range_index = prepare_data(data)
classes = special_sort(prepared_data, initial_point, final_point, space_between, first_tolerance)
final_data = make_classes(prepared_data, initial_point, space_between, error)
result = final_preparation(final_data)

result_for_diffrences = second_special_sort(prepared_data, initial_point, final_point, space_between, second_tolerance, classes)
final_data = make_classes(prepared_data, initial_point, space_between, error)
result = final_preparation(final_data)

############################################################################################################

result.to_csv(address_result_excel, index=False, header=False)
with open(address_result_txt, "w") as file:
    for index, row in result.iterrows():
        # Convert each row to a string and write to the file
        file.write(f"{row[0]}\t{row[1]}\n")

with open(diffrences_result_txt, "w") as file:
    for row in result_for_diffrences:
        # Convert each row to a string and write to the file
        file.write(f"{row[0]}\t{row[1]}\n")

with open(out_of_range_txt, "w") as file:
    for row in out_of_range_index:
        # Convert each row to a string and write to the file
        file.write(f"{row}\n")