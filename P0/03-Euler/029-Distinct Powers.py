a = range(2, 100+1)
b = range(2, 100+1)
result = []
for i in a:
    for j in b:
        temp = i**j
        result.append(temp)

result_set = set(result)
print(len(result_set))