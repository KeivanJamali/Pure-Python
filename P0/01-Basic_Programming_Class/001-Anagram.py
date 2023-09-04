def anagram(str):
    anag = []
    if len(str) == 1:
        return [str]
    else:
        strc = anagram(str[1:])
        for i in strc:
            for j in range(len(i)+1):
                final = i[:j] + str[0] + i[j:]
                if final not in anag:
                    anag.append(final)
        return anag

print(anagram("aabc"))