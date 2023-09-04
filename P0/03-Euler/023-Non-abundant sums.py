def factors(n: int) -> list:
    table = []
    for i in range(1, n):
        if divmod(n, i)[1] == 0:
            table.append(i)
    return table


def If_Ab(n: int) -> bool:
    if sum(factors(n)) > n:
        return True


def Ab_numbers(l1: list) -> list:
    Ab_numbers = []
    for i in l1:
        if If_Ab(i) == True:
            Ab_numbers.append(i)
    return Ab_numbers


def main() -> int:
    inp = 28123
    numbers = set(range(1, inp + 1))
    false_numbers = []
    ab_numbers = Ab_numbers(list(range(1, inp)))
    # print(ab_numbers)
    # print(len(ab_numbers))
    for i in range(len(ab_numbers)):
        for j in range(i, len(ab_numbers)):
            false_numbers.append(ab_numbers[i] + ab_numbers[j])
    answer = list(numbers - set(false_numbers))
    # print(answer)
    return sum(answer)


print(main())
