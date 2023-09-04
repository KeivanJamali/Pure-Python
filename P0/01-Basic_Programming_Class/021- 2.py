def main(main_list):
    len_list = []
    dic = {}
    # ans = pr(main_list)
    p = len(main_list)
    while len(len_list) < p:
        m = 0
        for i in range(len(main_list)):
            if m < len(main_list[i]):
                m = len(main_list[i])
                k = i
        len_list.append(main_list[k])
        main_list.pop(k)
    ans = pr(len_list)
    pp(ans)
    # print(main_list)
    # print(len_list)
    # for i in range(len(final)):
    #     dic[len_list[i][0]] = 0

def pp(ans):
    for i in ans:
        print(i[0], ((i[1]*10)//1)/10)


def pr(List):
    fin = []
    for i in range(len(List)):
        try:
            s = sum(List[i][1:]) / (len(List[i])-1)
            fin.append([List[i][0], s])
        except:
            pass
    # print(fin)
    return fin

n = input()
file = open(n, "r")
# file = open("a3.txt", "r")
List = []
for line in file.readlines():
    if line[-1] == "/n":
        line = line[:-1]
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    List.append(line)


# def n():
    # for
main(List)
