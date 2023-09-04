# first way
def findPermutations(string, i=0):
    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]
        findPermutations(words, i + 1)


# findPermutations('0123456789')

# seccond way
import itertools

inp = sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
answer = itertools.permutations(inp)
a = []
for i in answer:
    if len(a) == 1000000:
        break
    else:
        a.append(i)

print(a.pop())
