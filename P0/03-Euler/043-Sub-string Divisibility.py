from itertools import permutations

numbers = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
result = []
for num in numbers:
    # if num == (1, 4, 0, 6, 3, 5, 7, 2, 8, 9):
    # if num[0] != 0:
        if num[3]%2 != 0:
            # print("Hello 1")
            continue
        # print(num[2]+num[3]+num[4])
        if (num[2]+num[3]+num[4]) % 3 != 0:
            # print("Hello 2")
            continue

        if num[5] % 5 != 0:
            # print("Hello 3")
            continue

        if int(str(num[4]) + str(num[5]) + str(num[6])) % 7 != 0:
            # print("Hello 4")
            continue

        if int(str(num[5]) + str(num[6]) + str(num[7])) % 11 != 0:
            # print("Hello 5")
            continue

        if int(str(num[6]) + str(num[7]) + str(num[8])) % 13 != 0:
            # print("Hello 6")
            continue

        if int(str(num[7]) + str(num[8]) + str(num[9])) % 17 != 0:
            # print("Hello 7")
            continue

        temp = [str(i) for i in num]
        print(temp)
        result.append(temp)

sum_ = 0
for i in result:
    sum_ += int("".join(i))

print(sum_)
