my_file = open("D:\\progect\\pythonProject\\05-six hundred questions\\1.txt", "w")
while True:
    sent = input("sentence? ")
    if sent != "":
        sent += "\n"
        my_file.write(sent)
    else:
        break
my_file.close()