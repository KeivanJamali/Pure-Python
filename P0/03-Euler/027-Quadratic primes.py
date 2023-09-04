import Toolkit_Euler as tu


def len_make_pr(a: int, b: int, l: list, i=-1) -> int:
    while True:
        i += 1
        result = i ** 2 + a * i + b
        if result not in l:
            return i


result = 0
resulta = 0
resultb = 0
l = tu.prime_provid(1000)
for a in range(-1000, 1001):
    print("aaaaaaaaaa", a)
    for b in range(-1000, 1001):
        # print(b)
        temp = len_make_pr(a, b, l)
        if temp > result:
            result = temp
            resulta = a
            resultb = b


print(resulta)
print(resultb)
print(temp)

