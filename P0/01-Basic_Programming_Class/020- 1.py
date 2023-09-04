def make(s):
    s = s+' '
    s = list(s)
    dic = {}
    t = 1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            t+=1
        else:
            if dic.get(s[i],0) == 0:
                dic[s[i]] =t
                t = 1
            else:
                return "No"
    # print(dic)
    return check(dic)

def check(dic):
    m = 0
    l1 = []
    for k,v in dic.items():
        l1.append(v)
        if m < v:
            m = v
    l1 = sorted(l1)
    # print(l1)
    n = 0
    for i in range(len(l1)-1):
        if l1[i] + 1 == l1[i+1]:
            n += 1
    if n == len(l1)-1:
        for k , v in dic.items():
            if v == m:
                return k*v
    else:
        return "No"

n = input()
print(make(n))