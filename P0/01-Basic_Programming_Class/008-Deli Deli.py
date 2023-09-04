def check_solve(word: str) -> str:
    if word in note:
        return note[word]
    elif word[-1] == "y" and word[-2] not in l3:
        return seccond_rule(list(word))
    elif word[-1] in l or word[len(word) - 2:] in l2:
        word += "es"
    else:
        word += "s"
    return word                     #Keip S


def seccond_rule(word: list) -> str:
    word.pop()
    word = "".join(word)
    word += "ies"
    return word


first_line = input().split()
first_line[0] = int(first_line[0])
first_line[1] = int(first_line[1])
# __________________________________________
note = {}
for i in range(first_line[0]):
    temp = input().split()
    note[temp[0]] = temp[1]
# __________________________________________
given_words = []
for i in range(first_line[1]):
    given_words.append(input())                     #Keip S
# __________________________________________
l = ["o", "s", "x"]
l2 = ["ch", "sh"]
l3 = ["a","e","i","y","o"]

for i in given_words:
    print(check_solve(i))