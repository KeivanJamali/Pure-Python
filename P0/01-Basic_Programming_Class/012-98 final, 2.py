def change(given: dict) -> dict:
    newdict = {}
    final_dict = {}
    for k, v in given.items():
        if newdict.get(v, 0) == 0:
            newdict[v] = [k]
        else:
            newdict[v].append(k)
        print(newdict)
        print(str(v)+"-->"+str(k))
        for kn, vn in given.items():
            if vn == k:
                newdict[v].append(kn)
                newdict[vn] = 0
        # print(newdict)
    for k, v in newdict.items():
        if v != 0:
            final_dict[k] = v
    return final_dict

print(change({3: 2, 2: 1, 4: 1, 6: 7, 11: 7, 7: 5, 8: 5, 10: 19}))
