a = "today is 23-08-2025. I want to go to downtown at 21:30.".lower()
b = "1234567890"
c = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            c = c + 1


print(c)
