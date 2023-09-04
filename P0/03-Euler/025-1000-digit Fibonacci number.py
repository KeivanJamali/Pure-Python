i = -1
fibo = [1, 1]
while True:
    print(i)
    i += 1
    s = fibo[i] + fibo[i+1]
    fibo.append(s)
    # print(s)
    if len(list(str(s))) == 1000:
        break

print(fibo)
print(len(fibo))
print(fibo.pop())
