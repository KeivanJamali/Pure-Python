def calculate_matrix(matrix):
    under_dic = {}
    for i in range(len(matrix)):
        under_dic[i] = [i]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                if j not in under_dic[i]:
                    under_dic[i].append(j)
                if i not in under_dic[j]:
                    under_dic[j].append(i)
    return under_dic


def if_is_good_or_not(under_dic, s, n):
    main = []
    b = 0
    miss = []
    for i in s:
        for j in under_dic[i]:
            main.append(j)
    for i in range(n):
        if i in main:
            b += 1
        else:
            miss.append(i)
    if b == n:
        return True
    else:
        return miss


def it_is_good(under_dic, s: set, bed, n):
    new_s = []
    for i in s:
        b = s.copy()
        b = b - {i}
        if if_is_good_or_not(under_dic, b, n) == True:
            new_s.append(bed[i])
    if bool(new_s) == True:
        return s - {bed.index(max(new_s))}
    else:
        return s


def it_isnt_good(under_dic, s: set, bed, n, miss):
    make_good_s_list = []
    for i in range(len(under_dic)):
        if set(miss) < set(under_dic[i]):
                make_good_s_list.append(bed[i])
    return s.union({bed.index(min(make_good_s_list))})



def main(n: int, matrix: list, bed: list, s: set):
    dic = calculate_matrix(matrix)
    Bool = if_is_good_or_not(dic, s, n)
    if Bool == True:
        new_s = it_is_good(dic, s, bed, n)
    else:
        new_s = it_isnt_good(dic, s, bed, n, Bool)
    return new_s


print(main(4,[[0, 1, 1, 1],
[1, 0, 1, 1],
[1, 1, 0, 0],
[1, 1, 0, 0]],[2, 4, 1, 5],{0,1}))
