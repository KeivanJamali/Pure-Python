n = input()
s = ""
w = 1
SUM = 0
for i in range(len(n) - 1, -1, -1):
    s += n[i]

for i in s:
    SUM = SUM + int(i) * w
    w = w * 2

print(SUM)
