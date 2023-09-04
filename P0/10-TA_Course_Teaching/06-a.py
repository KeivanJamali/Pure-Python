def fib(n: int, pos=0) -> tuple:
    if n == 1:
        line = [1]
        if pos == 0:
            sum = 1
        else:
            sum = 0
    else:
        (p_line, sum) = fib(n - 1, pos+1)
        line = [1]
        for i in range(len(p_line) - 1):
            line.append(p_line[i] + p_line[i + 1])
        line.append(1)
        if pos < len(line):
            sum += line[pos]
    return tuple((line, sum))

print(fib(7))


