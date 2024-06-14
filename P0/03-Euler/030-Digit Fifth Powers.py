from itertools import product
pow = 5
result = []
for i in range(2, 7):
    all_comb = product(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], repeat=i)
    for comb in all_comb:
        comb2 = tuple(("1", "6", "3", "4"))
        done = False
        temp = 0
        number = int("".join(list(comb)))
        for c in str(number):
            temp += int(c)**pow
        if int(temp) == int(number):
            if len(str(temp)) > 1:
                temp3 = number
                result.append(temp3)
result_set = set(result)
print(sum(result_set))
