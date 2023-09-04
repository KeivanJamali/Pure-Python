t = int(input())
b, d = [], []
for i in range(t):
    b.append(input())
for i in range(t):
    L = list(b[i])
    for j in range(10):
        c = 0
        while True:
            if str(j) in L:
                c += 1
                L.remove(str(j))
            else:
                break
        if c > 3:
            d.append(i + 1)
            break
    ################################
    for j in range(0, 5):
        L = list(b[i])
        k = j + 3
        if L[j] == L[j + 1] == L[j + 2]:
            d.append(i + 1)
    ################################
    c = 0
    for j in range(4):
        if b[i][j] == b[i][7 - j]:
            c += 1
    if c == 4:
        d.append(i + 1)

for i in range(1, t + 1):
    if i in d:
        print("Ronde! ")
    else:
        print("Rond Nist ")
