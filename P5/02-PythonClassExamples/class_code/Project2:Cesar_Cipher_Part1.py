alphabet = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L":12, "M": 13, "N": 14, "O": 15, "P":16,
            1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P"}

text = input("Write your sentence please: ")
code = int(input("What is your code (int)? "))

text = "".join(text.split(" "))
coded_text = ""
for letter in text:
    new_letter_number = alphabet[letter] + code
    new_letter = alphabet[new_letter_number]
    coded_text += new_letter

print(coded_text)
