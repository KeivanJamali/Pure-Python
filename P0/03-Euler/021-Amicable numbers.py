def amicable_check(n1: int, n2: int, sm: list) -> bool:
    if sm[n1] == n2 and sm[n2] == n1 and n1 != n2:
        return True
    else:
        return False


def sumd_factors(n: int) -> int:
    i = 1
    List = []
    List2 = [2]  # greater than 1 is OK
    Bool = True
    while i < min(List2) or Bool == True:
        if Bool == True:
            List2 = []
            Bool = False
        if n % i == 0:
            List.append(i)
            List2.append(n // i)
        i += 1
    return sum(List) + sum(List2) - n


def main(n: int) -> int:
    answer = []
    SUM_LIST = []
    for i in range(n):
        SUM_LIST.append(sumd_factors(i))
    for i in range(1, n):
        for j in range(i + 1, n):
            if amicable_check(i, j, SUM_LIST) == True:
                answer.append(i)
                answer.append(j)
    return sum(answer)


print(main(1000))
