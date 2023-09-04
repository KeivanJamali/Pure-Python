a = 2**1000
print(a)
a = list(str(a))
for i in range(len(a)):
    a[i] = int(a[i])
print(sum(a))
