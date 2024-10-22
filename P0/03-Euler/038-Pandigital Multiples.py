def check(number):
    if len(str(number)) != 9:
        return False
    chars = []
    for char in str(number):
        if char == "0":
            return False
        if not char in chars:
            chars.append(char)
        else:
            return False
    return True

def transform(x):
    res_n = ""
    numbers = []
    for i in range(1, 6):
        res_n += str(i*x)
        numbers.append([int(res_n), i])
    return numbers

try_numbers = [9]
for i in range(90, 100):
    try_numbers.append(i)
for i in range(900, 1000):
    try_numbers.append(i)
for i in range(9000, 10000):
    try_numbers.append(i)

result = []
for i in try_numbers:
    numbers_5 = transform(i)
    for num in numbers_5:
        if check(num[0]):
            result.append([i, num[1], num[0]])


print(result)   