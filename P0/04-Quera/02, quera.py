n = int(input())
Input = list(input())
hol_sum = 0
for i in range(n-1):
    Input.remove(" ")
print(Input)

def sumi(x, y):
    s=0
    for i in range(y-x+1):
        s += x + i
    return s

for i in range(n):
    for j in range(i, n):
        sum = sumi(int(Input[i]), int(Input[j]))
        hol_sum += sum
print(hol_sum)