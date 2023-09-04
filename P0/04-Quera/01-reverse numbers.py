List = []
while True:
    n = int(input())
    if n == 0:
        break
    List.append(n)
for i in range(len(List) - 1, -1, -1):
    print(List[i])
