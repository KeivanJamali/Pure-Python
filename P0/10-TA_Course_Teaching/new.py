def find(Dic:dict):
    names = []
    for k, v in Dic.items():
        a = True
        for i in range(len(v)):
            if v[i][0] == 20:
                a = False
                break
        if a == True:
            for i in range(len(v)):
                names.append(v[i][1])
    return names


n = int(input())
Dict = {}
name = []

for i in range(n):
    a = True
    b = True
    In = input().split()
    name.append(In[0])
    for k, v in Dict.items():
        if In[1] == k:
            for i in range(len(Dict[k])):
                if In[2] == Dict[k][i][0]:
                    Dict[k][i].append(In[0])
                    a = False
            if a == True:
                Dict[k].append([int(In[2]), In[0]])
            # print(Dict)
            b = False
    if b == True:
        Dict[In[1]] = [[int(In[2]), In[0]]]

ans = find(Dict)
# print(Dict)
# print(ans)
name = set(name)
ans = set(ans)
print(len(name - ans))
