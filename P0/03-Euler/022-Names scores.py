file = open("p022_names.txt", "r").read().upper().split(",")
so_file = sorted(file)
print(so_file)
init_v = ord("A") - 1

answer = 0
for i in range(len(so_file)):
    s = 0
    for j in range(1, len(so_file[i]) - 1):
        s += ord(so_file[i][j]) - init_v
    m = s * (i+1)
    answer += m
print(answer)
