a = "Hello, today is 1404/5/6 and It is so warm and hot.".lower()
s = 0
vowels = {'a', 'e', 'i', 'o', 'u'}
for letter in a:
    if letter in vowels:
        s = s + 2

print(s)
