def real_find(List: list) -> list:
    result = []
    for i in List:
        if i not in result:
            result.append(i)
    return result


def repeat(List: list, n: int) -> int:
    sum = 0
    for i in List:
        if n == i:
            sum += 1
    return sum


def calc_list(a: list) -> list:
    help_list = real_find(a)
    rep_list = []
    result = []
    for i in help_list:
        rep_list.append(repeat(a, i))
    rep_help_list = real_find(rep_list)
    for i in sorted(rep_help_list):
        temp = []
        for j in range(len(rep_list)):
            if i == rep_list[j]:
                temp.append(help_list[j])
        result.append(tuple((i, sorted(temp))))
    return result

print(calc_list([4, 1, 7, 4, 1, 7, 5]))