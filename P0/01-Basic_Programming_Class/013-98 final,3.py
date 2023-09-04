def f(z, n):
    x = []
    for i in range(n + 1):
        a = "+" * i + "-" * (n - i)
        x += jaigasht(a)
    for i in x:
        if i not in z:
            z.append(i)
    check(z)


def check(z) -> None:
    # print(z)
    x = z.copy()
    for i in x:
        # print(i)
        i = list(i)
        for j in range(len(i)-2):
            try:
                if i[j] == i[j+1] == i[j+2]:
                    # print(i)
                    z.remove(list_to_str(i))
                    # print("removed")
                    # print()
                    # print("helo")
                else:
                    pass
                    # print("not removed", i)
            except:
                continue
    return z

def list_to_str(List):
    s = ''
    for i in List:
        s+=i
    return s

def jaigasht(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
    ag = jaigasht(s[1:])
    for w in ag:
        for pos in range(len(w) + 1):
            t = w[:pos] + s[0] + w[pos:]
            result.append(t)
    return result


n = 4
z = []
f(z, n)
print(z)
