"""find Fibonacci numbers by Pascal's triangle."""


def fib(n: int, pos=0) -> tuple:
    if n == 1:
        line = [1]
        if pos == 0:
            result = 1
        else:
            result = 0
    else:
        line = [1]
        (past_line, result) = fib(n - 1, pos + 1)
        for i in range(len(past_line) - 1):
            line.append(past_line[i] + past_line[i + 1])
        line.append(1)
        if pos < len(line):
            result += line[pos]
    return (line, result)


print(fib(7))
