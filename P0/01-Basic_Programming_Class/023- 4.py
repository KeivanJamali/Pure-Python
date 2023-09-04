from random import Random
import time

m = 0


def wow(main_list, a, b, s):
    global m
    t1 = time.time()
    q = 0
    my_final = []
    for i in main_list:
        if i[0] == i[1]:
            main_list.remove(i)
    print(main_list)
    # while True:
    for i in range(3):
        m = 0
        l = [a]
        my_find = dodo(main_list, a, b, l)
        if q < my_find[1]:
            q = my_find[1]
            my_final = my_find.copy()
        t2 = time.time()
        print(my_find, my_final)
        print(t2-t1)
        if t2 - t1 >= s:
            print(t2-t1)
            return my_final


def dodo(main_list, a, b, ans):
    global m
    while True:
        temp1 = main_list[Random().randrange(0, len(main_list))]
        t = Random().randrange(0, 2)
        if temp1[t] == a:
            # print("     ", temp1)
            ab = temp1[1 - t]
            ans.append(ab)
            m += temp1[2]
            if ab == b:
                # ans.append(b)
                return [ans, m]
            else:
                main_list.remove(temp1)
                return dodo(main_list, ab, b, ans)


wow([(1, 1, 6), (1, 2, 5), (1, 4, 7), (2, 6, 3), (6, 9, 4), (4, 9, 10)], 1, 9, 0.1)
