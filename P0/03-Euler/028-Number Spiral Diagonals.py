# 1, | 3, 5, 7, 9 | -11-, 13, -15-, 17, -19-, 21, -23-, 25 | -27-, -29-, 31, -33-, -35-, 37, -39-, -41-, 43, -45-, -47-, 49

n = 1001
count = 1001*1001

odd = range(1, count+1, 2)
c_main = 0
c_cycles = 0
c_numbers_in_cycles = 0
i = 0
result = [1]
while True:
    if i + c_main+1 + (c_main+1) * c_cycles >= len(odd):
        break
    if c_main == 4:
        c_main = 0
        c_cycles += 1
        i += 4*c_cycles
    elif c_main!= 4:
        c_main += 1
        result.append(odd[i + c_main + c_main * c_cycles])

print(sum(result))