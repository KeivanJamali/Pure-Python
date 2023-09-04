def pascal(n: int) -> list:
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        line = [1]
        p_line = pascal(n-1)
        for i in range(len(p_line)-1):
            line.append(p_line[i]+p_line[i+1])
        line.append(1)
    return line

print(pascal(5))
