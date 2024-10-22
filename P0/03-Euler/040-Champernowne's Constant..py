i = 0
string = ""
while True:
    i += 1
    string += str(i)
    if len(string) > 1000_000:
        break


print(int(string[0])*int(string[10-1])*int(string[100-1])*int(string[1000-1])*int(string[10000-1])*int(string[100000-1])*int(string[1000_000-1]))
