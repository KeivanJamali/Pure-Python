def order(List: list) -> list:
    e = []
    m = []
    h = []
    for i in List:
        if i[1] == "e":
            e.append(i[0])
        elif i[1] == "m":
            m.append(i[0])
        elif i[1] == "h":
            h.append(i[0])
    ans = []
    for i in e:
        a = (i, "e")
        ans.append(a)
    for i in m:
        a = (i, "m")
        ans.append(a)
    for i in h:
        a = (i, "h")
        ans.append(a)
    return ans

print(order([('dab', 'h'), ('cry', 'e'), ('die', 'e'), ('err', 'm'), ('hay', 'h'), ('zoo', 'e'), ('ego',
'm'), ('fee', 'm'), ('era', 'h'), ('eye', 'e')]))