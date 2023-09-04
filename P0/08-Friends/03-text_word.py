def count(text: str, word: str):
    l = len(word)
    text = text.lower()
    text = " " + text + " "
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    c = 0
    for i in range(len(text) - l):
        if text[i:i + l] == word:
            n_word = text[i - 1:i + l + 1]
            print(n_word)
            if n_word[0] not in letters and n_word[-1] not in letters:
                c += 1
    if c == 0:
        print("There is no " + word + " in the text!")
    else:
        print("In the text this " + word + " repeated " + str(c) + " times!")


t = "And Bankside -and were the Bear and the Paris Gardens, ands used for the popular sport of bear and bull baiting; and the Globe theatre, the scene of the production of many of Shakespeare’s plays for fifteen years after its erection in 1599."
w = "and"
t2 = "Not just that you went to a certain address but that the address was a movie theater and—based on where you sat and that you ordered tickets online—you saw Episode VII of Star Wars."
w2 = "cinema"
count(t, w)
count(t2, w2)
