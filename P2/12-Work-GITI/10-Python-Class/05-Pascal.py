"""Write a function which implements the Pascal's triangle..."""


def pascal(n: int) -> list:
    if n == 1:
        return [1]
    else:
        p_line = pascal(n - 1)
        line = [1]
        for i in range(len(p_line) - 1):
            line.append(p_line[i] + p_line[i + 1])
        line.append(1)
    return line


for i in range(1, 10):
    print(pascal(i))
