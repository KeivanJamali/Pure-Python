def collatz(num):
    temp = 1
    n = num
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            temp += 1
        else:
            n = 3 * n + 1
            temp += 1
    # dic[n] = temp
    if List[1] < temp:
        List[0] = num
        List[1] = temp


number = 3
dic = {}
List = [0, 0]
while number <= 1000000:
    collatz(number)
    number += 1
print(List)