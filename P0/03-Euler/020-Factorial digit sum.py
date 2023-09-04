def Fact(n: int) -> int:
    m = 1
    for i in range(1, n+1):
        m *= i
    return m

print(Fact(100))

Lst = list(str(Fact(100)))
s = 0
for i in Lst:
    s += int(i)
print(s)