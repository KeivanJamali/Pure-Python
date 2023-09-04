def bn(x: int):
    result = ""
    while True:
        temp = x % 2
        x //= 2
        result = str(temp) + result
        if x == 1:
            result = str(1) + result
            break
        elif x == 0:
            break
    return result


def bn2(x: float, n: int):
    result = "."
    for i in range(n):
        temp = int(x * 2)
        x = (x * 2) % 1
        result = result + str(temp)
    return result


def find_in_binary(x):
    if type(x) == int:
        print(bn(x))
    if type(x) == float:
        print(bn(int(x)) + bn2(x % 1, 6))


find_in_binary(2.7)
