file_name = input("what file?")
my_file = open(file_name, "r")
while True:
    line = my_file.readline()
    if line != "":
        print(line, end="")
    else:
        my_file.close()
        break

