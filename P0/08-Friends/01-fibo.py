def fib(n: int) -> list:
    my_complete_num = [1, 2]
    while my_complete_num[-1] < n:
        l = len(my_complete_num)
        my_complete_num.append(my_complete_num[l - 1] + my_complete_num[l - 2])
    my_complete_num.pop()
    return my_complete_num


def sum_E(complete: list) -> int:
    Sum = 0
    for i in complete:
        if i % 2 == 0:
            Sum += i
    return Sum


print(sum_E(fib(4000000)))