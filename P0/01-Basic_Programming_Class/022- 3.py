l1 = []


def masir(main_dic):
    global l1

    dic = {}
    # a = "a"
    for k, v in main_dic.items():
        l1 = []
        # print(a)
        # if k not in dic[a]:
        l1.append(k)
        l1.append(v)
        # print("the v is", v, "list", l1)
        p = find(main_dic, v)
        if p == False:
            if dic.get(0, 0) == 0:
                dic[0] = [k, v]
            else:
                dic[0].append(v)
                dic[0].append(k)
        else:
            a = min(p)
            # print(p)
            # print(a)
            dic[a] = set(p)
    return corroct(dic)


def find(main_dic, n):
    if n == l1[0]:
        # print("hey")
        return l1
    for k, v in main_dic.items():
        if k == n:
            l1.append(v)
            return find(main_dic, v)
    # print("say")
    return False

def corroct(dic):
    v = dic[0]
    v = set(v)
    dic[0] = v
    return dic


print(masir({11: 7, 3: 4, 2: 5, 4: 3, 5: 8, 8: 2, 7: 9, 10: 9, 6: 1, 12: 7}))
