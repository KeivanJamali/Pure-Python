n = int(input())
refrence = []
results = {}
for i in range(n):
    refrence.append(input()[0])
letters = set(refrence)
for i in letters:
    c = 0
    for j in range(len(refrence)):
        if i == refrence[j]:
            c += 1               #Keip S
    results[i] = c
s = []
for k, v in results.items():
    if v > 4:
        s.append(k)
if bool(s) == False:
    print("PREDAJA")
else:
    print("".join(sorted(s)))
