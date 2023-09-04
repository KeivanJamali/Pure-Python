import decimal
from decimal import Decimal
decimal.getcontext().prec = 4000
tt = 0
# print(decimal.getcontext())


def reciprocal(n: list) -> list:
    new_list = []
    for i in range(len(n)//4):
        new_list.append(n[i])
        if new_list == n[len(new_list):2*len(new_list)] and new_list == n[2*len(new_list):3*len(new_list)] and new_list == n[3*len(new_list):4*len(new_list)]:
            # print(new_list)
            return new_list
    n2 = n.copy()
    n2.pop(0)
    # print("go in 2")
    # print(n2)
    return reciprocal(n2)


for d in range(983, 984):
    l = Decimal(1) / Decimal(d)
    # print(l)
    check = list(str(l))
    if len(check) < 20:
        pass
    else:
        check2 = check[2:len(check)]
        # print(check2)
        ans = reciprocal(check2)
        t = len(ans)
        if tt < t:
            tt = t
            print(d)
print("the answer:")
print(tt)
