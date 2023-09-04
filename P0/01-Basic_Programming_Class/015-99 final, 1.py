def main(sery: str) -> list:
    j = 3
    ans = []
    while j <= len(sery):
        j += 2
        for i in range(len(sery) - j + 1):
            # print(i)
            new = sery[i:i + j]
            # print(new)
            if check(new, j) == True:
                ans.append(new)
                # print(ans)
    return ans


def check(st: str, n: int) -> bool:
    b1, b2 = 0, 0
    n = n // 2
    st_1_a = st[:n]
    st_1_b = st[n:]
    st_2_a = st[:n + 1]
    st_2_b = st[n + 1:]
    # print("1 start")
    for i in range(len(st_1_b)):
        temp = st_1_b[:i] + st_1_b[i + 1:]
        # print(temp)
        if temp == st_1_a:
            # print("b1")
            b1 += 1
    # print("2 start")
    for i in range(len(st_2_a)):
        temp = st_2_a[:i] + st_2_a[i + 1:]
        # print(temp)
        if temp == st_2_b:
            # print("b2")
            b2 += 1
    if b1 == 1 and b2 == 0:
        return True
    if b1 == 0 and b2 == 1:
        return True


print(main("aababcabc"))
