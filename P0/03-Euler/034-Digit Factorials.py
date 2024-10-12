from math import factorial

factorials = [factorial(i) for i in range(10)]
n_digit = {"9":[7, 6], "8":[6, 5], "7":[5, 6], "6":[4, 3], "5":[3], "4":[2], "3":[1]}

def find():
    result = []
    for i in range(9, 2, -1):
        start, end = boundary(i)
        # print(start, end, i)
        for j in range(start, end+1):
            if j == fac2(j):
                result.append(j)
    return result

def boundary(a):
    _min = max((min(n_digit[str(a)])-1) * 1 + factorials[a], int(str(1)+(min(n_digit[str(a)])-2)*"0" + str(a)))
    _max = min(factorials[a] * (max(n_digit[str(a)])), int(str(a)* max(n_digit[str(a)])))
    return [_min, _max]

def fac2(number):
    d = list(str(number))
    result = 0
    for i in d:
        result += factorials[int(i)]
    return result

res = find()
print(res)
print(sum(res))
