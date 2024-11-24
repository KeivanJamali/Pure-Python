file_path = "D:/All Python/Pure-Python/P0/03-Euler/p042_words.txt"
with open(file_path, "r") as file:
    text = file.read()

letters = [chr(i) for i in range(65, 91)]

words = text.split(",")

triangle = [0]
n = 0
while triangle[-1] < 416:
    n += 1
    temp = 0.5 * n * (n+1)
    triangle.append(temp)

correct = 0
for word in words:
    sum_ = 0
    for i in range(1, len(word)-1):
        sum_ += letters.index(word[i])+1
    
    if sum_ in triangle:
        correct += 1

print(correct)