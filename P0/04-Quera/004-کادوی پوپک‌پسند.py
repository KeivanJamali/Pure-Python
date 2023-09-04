def all_divisor(n: int) -> list:
    if n == 1:
        return [1]
    else:
        all_d = []
        every = list(range(n, 0, -1))
        while every:
            temp = every.pop()
            if n % temp == 0:
                all_d.append(temp)
                all_d.append(n // temp)
                every.remove(n // temp)
        return sorted(all_d)


def split_it(line: str, n: int) -> list:
    result = []
    length = len(line) // n
    for i in range(n):
        result.append(line[length * i:length * (i + 1)])
    return result


def and_binary(dif: list) -> int:
    c = int(dif[0])
    for i in range(1, len(dif)):
        c &= int(dif[i])
    return c


def main(field: str):
    l1 = all_divisor(len(field))
    m = 0
    for i in l1:
        temp = and_binary(split_it(field, i))
        if m < temp:
            m = temp
    return m


n = input()
print(main(n))
