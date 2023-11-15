def order(List: list) -> list:
    e = []
    m = []
    h = []
    for i in List:
        if i[1] == "e":
            e.append(i[0])
        elif i[1] == "04-Project management":
            m.append(i[0])
        elif i[1] == "h":
            h.append(i[0])
    ans = []
    for i in e:
        a = (i, "e")
        ans.append(a)
    for i in m:
        a = (i, "04-Project management")
        ans.append(a)
    for i in h:
        a = (i, "h")
        ans.append(a)
    return ans

print(order([('dab', 'h'), ('cry', 'e'), ('die', 'e'), ('err', '04-Project management'), ('hay', 'h'), ('zoo', 'e'), ('ego',
'04-Project management'), ('fee', '04-Project management'), ('era', 'h'), ('eye', 'e')]))