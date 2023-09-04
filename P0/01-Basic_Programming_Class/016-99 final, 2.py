def find(main_list: list) -> list:
    g_1_list = {}
    g_2_list = {}
    for i in main_list:
        try:
            if bool(g_1_list[len(i)]) != True:
                g_1_list[len(i)] = i
            else:
                g_2_list[len(i)] = i
        except:
            g_1_list[len(i)] = i
    print(g_1_list)
    print(g_2_list)
    return make_matrix(g_1_list, g_2_list)


def change_row_to_column(d: dict) -> dict:
    new_dic = {}
    for i in range(len(d)):
        new_dic[i] = []
        for v in d.values():
            new_dic[i].append(v[i])
    return new_dic


def make_matrix(g1: dict, g2: dict) -> dict:
    dic = {}
    b = True
    j = 0
    for i in range(len(g1)):
        dic[i] = []
    # print(dic)
    for j in range(len(g1)):
        # b = True
        for i in range(len(g1)):
            i = i - j
            for k1, v1 in g1.items():
                if k1 == len(g1) and b == True:
                    dic[j].append(v1[j])
                    b = False
                for k2, v2 in g2.items():
                    if k2 == k1 == len(g1) - i:
                        dic[j].append(min(v1[j], v2[j]))
                        dic[i + j].append(max(v1[j], v2[j]))
    return dic


def main():
    file = open("a1.txt", "r")
    main_list = []
    for line in file.readlines():
        line = line[:-1]
        line = line.split()
        for i in range(len(line)):
            line[i] = int(line[i])
        if bool(line) == True:
            main_list.append(line)
    return change_row_to_column(find(main_list))


print(main())
