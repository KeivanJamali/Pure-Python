def find_prime(table: list, s_point: tuple, f_point: tuple, way: str, did_points) -> str:
    f_points = [(s_point[0], s_point[1] + 1, "R"), (s_point[0], s_point[1] - 1, "L"), (s_point[0] + 1, s_point[1], "D"),
                (s_point[0] - 1, s_point[1], "U")]

    ###############################
    for i in f_points:
        if (i[0], i[1]) in did_points:
            # print("tekrari: ", i[0], i[1])
            continue
        if if_prime(table[i[0]][i[1]]) == True:
            # print("prime val for point: ", i[0], i[1], i[2])
            did_points.append(s_point)
            # print("now did_point is: ", did_points)
            way += i[2]
            if (i[0], i[1]) == f_point:
                # print("The End", way[1:])
                # print("did_point == ", did_points)
                return way[1:]
            return find_prime(table, (i[0], i[1]), f_point, way, did_points)


def if_prime(n: int) -> bool:
    if n <= 1:
        return False
    main_list = set(range(n - 1, 1, -1))
    while main_list:
        temp = main_list.pop()
        if n % temp == 0:
            return False
        else:
            main_list = main_list - set(range(2 * temp, n, temp))
    return True


def make_matrix() -> list:
    n = int(input())
    matrix = []
    # ____________________________________
    temp0 = "0 " * (n + 2)
    temp0 = temp0.split()
    for j in range(len(temp0)):
        temp0[j] = int(temp0[j])
    matrix.append(temp0)
    # ____________________________________
    for i in range(n):
        temp = input()
        temp = "0 " + temp + " 0"
        temp = temp.split()
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        matrix.append(temp)
    # ____________________________________
    matrix.append(temp0)
    return matrix


def main():
    answers = []
    t = int(input())
    for i in range(t):
        main_matrix = make_matrix()
        temp = input().split()
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        start = (temp[0] + 1, temp[1] + 1)
        #############################
        temp = input().split()
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        finish = (temp[0] + 1, temp[1] + 1)
        s = "N"
        did = []
        way = find_prime(main_matrix, start, finish, s, did)
        if way:
            answers.append(way)
        else:
            # TODO: hello
            answers.append("No Monaseb Masir!")
    return answers


p = main()
# print("PPPPPPP iiiiiiiiiiiiiiiiiiiiiiiiiiissssssssssssssssssssss::::", p)
for i in p:
    print(i)