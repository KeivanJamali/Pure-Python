def same_find(List: list) -> list:
    new_list = []
    num_list = []
    for i in range(len(List)):
        if len(List[i]) not in num_list:
            new_list.append([list(List[i])])
            num_list.append(len(List[i]))
        else:
            for j in range(len(new_list)):
                if len(List[i]) == len(new_list[j][0]):
                    new_list[j].append(list(List[i]))
        # print(num_list)

    return new_list


def check(List: list):
    letters = List[0]
    result = []
    for i in letters:
        sum = 0
        new_list = List[:]
        # print("new list: ", new_list)
        # print("main list: ", List)
        check_word = new_list[0].copy()
        check_word.remove(i)
        # print("check: ",check_word)
        for j in range(1, len(new_list)):
            word = new_list[j].copy()
            word.remove(i)
            if word == check_word:
                sum += 1
                result.append([i, check_word, sum])
                # print("result: ", result)
                # print("newList: ", new_list)
    return result


def same(List):
    result = [[List[0]]]
    for i in range(1, len(List)):
        Bool = True
        for j in List[i]:
            if Bool == False:
                break
            for k in range(len(result)):
                if j not in result[i][0]:
                    result.append([List[i]])
                    Bool = False
                    break




a = ["bac", "ba", "cba"]
a2 = ["cdba", "cbad", "dbca", "dbac"]
a3 = ["%yzvh", "%yvzh", "xrmz", "zxrm", "rs1a", "rsa1"]
b = same_find(a3)
for i in b:
    print(i)
# for i in b:
#     c = check(i)
# print(c)
