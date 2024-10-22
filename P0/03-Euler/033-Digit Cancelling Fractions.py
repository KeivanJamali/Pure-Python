import math

result = []
for i in range(10, 100):
    for j in range(i+1, 100):
        if not str(j)[1] == "0":
            answer = i/j
            upp = i
            dom = j
            i1 = int(str(i)[0])
            i2 = int(str(i)[1])
            j1 = int(str(j)[0])
            j2 = int(str(j)[1])
            if i1 == j1:
                if j2 != 0 and abs(i2/j2 - answer) < 0.000001:
                    print(upp, " and ", dom)
                    result.append(upp/dom)
            if i1 == j2:
                if j1 !=0 and abs(i2/j1 - answer) < 0.000001:
                    print(upp, " and ", dom)
                    result.append(upp/dom)
            if i2 == j1:
                if j2 != 0 and abs(i1/j2 - answer) < 0.000001:
                    print(upp, " and ", dom)
                    result.append(upp/dom)
            if i2 == j2:
                if j1 != 0 and abs(i1/j1 - answer) < 0.000001:
                    print(upp, " and ", dom)
                    result.append(upp/dom)
print(result)
print(math.prod(result))