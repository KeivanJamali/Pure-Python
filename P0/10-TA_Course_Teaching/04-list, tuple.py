def real_find(List: list) -> list:
    result_list = []
    for i in List:
        if i not in result_list:
            result_list.append(i)
    return result_list


def repeat(List: list, n: int) -> int:
    result_rep = 0
    for i in List:
        if n == i:
            result_rep += 1
    return result_rep


def calc_list(List: list) -> list:
    help_list = real_find(List)
    repeat_list = []
    last_result = []
    for i in help_list:
        repeat_list.append(repeat(List, i))
    rep_help_list = real_find(repeat_list)
    for i in sorted(rep_help_list):
        temp = [i]
        for j in range(len(repeat_list)):
            if i == repeat_list[j]:
                temp.append(help_list[j])
        # print(temp)
        last_result.append(tuple((temp[0], sorted(temp[1:]))))
    return last_result

a = [4, 1, 7, 4, 7, 1, 5]
b = calc_list(a)
print(b)