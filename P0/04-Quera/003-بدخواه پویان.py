n = input().split()
p = int(n[0])
d = int(n[1])
i = 0
while True:
    i += 1
    if (d*i)%p <= p/2:
        break
print(d*i)