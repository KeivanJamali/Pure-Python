from tabulate import tabulate

alphabet = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
    "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
    "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26,

    "a": 27, "b": 28, "c": 29, "d": 30, "e": 31, "f": 32, "g": 33, "h": 34, "i": 35, "j": 36,
    "k": 37, "l": 38, "m": 39, "n": 40, "o": 41, "p": 42, "q": 43, "r": 44, "s": 45,
    "t": 46, "u": 47, "v": 48, "w": 49, "x": 50, "y": 51, "z": 52,

    " ": 53,

    1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J",
    11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S",
    20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z",

    27: "a", 28: "b", 29: "c", 30: "d", 31: "e", 32: "f", 33: "g", 34: "h", 35: "i", 36: "j",
    37: "k", 38: "l", 39: "m", 40: "n", 41: "o", 42: "p", 43: "q", 44: "r", 45: "s",
    46: "t", 47: "u", 48: "v", 49: "w", 50: "x", 51: "y", 52: "z",

    53: " "
}



class Cesar_Cipher:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.max_number_possable = max(k for k in self.dictionary.keys() if isinstance(k, int))


    def show_dict(self):
        print(tabulate(self.dictionary.items(), headers=["Key", "Value"]))

    def code_text(self, text: str, key: int):
        print(f"[INFO] Start to make a code for you 🙂.")
        result = ""
        for letter in text:
            n_related_to_letter = self.dictionary[letter]
            n_related_to_letter += key
            while n_related_to_letter > self.max_number_possable:
                n_related_to_letter -= self.max_number_possable
            result += self.dictionary[n_related_to_letter]
        print(f"[INFO] Your code is ready: '{result}' 🔥.")
        return result
    
    def decode_text(self, text: str, key: int=None):
        if key:
            print(f"[INFO] Try to decode '{text}' for you 💻️...")
            resuls = ""
            for letter in text:
                n_related_to_letter = self.dictionary[letter]
                n_related_to_letter -= key
                while n_related_to_letter < 1:
                    n_related_to_letter += self.max_number_possable
                resuls += self.dictionary[n_related_to_letter]
            print(f"[INFO] Alright, are you ready 😁?\n Here you are: '{resuls}' 🤞.")
            return resuls
        else:
            print(f"[INFO] Oh no, you don't have any key 🤦‍♂️. Don't worry 🦇! \nI will decode it for you and give you the key too 😎.")
            all_results = []
            for i in range(1, self.max_number_possable + 1):
                result = ""
                for letter in text:
                    n_related_to_letter = self.dictionary[letter]
                    n_related_to_letter -= i
                    while n_related_to_letter < 1:
                        n_related_to_letter += self.max_number_possable
                    result += self.dictionary[n_related_to_letter]
                if i % 3 == 0:
                    all_results[-1] = all_results[-1] + [i, result]
                elif i % 3 == 1:
                    all_results.append([i, result])
                elif i % 3 == 2:
                    all_results[-1] = all_results[-1] + [i, result]

            print(tabulate(all_results, headers=["Key", "Decoded Text", "Key", "Decoded Text", "Key", "Decoded Text"], tablefmt="grid"))
            print(f"[INFO] Now you can see which one has meaning. That is what you want 😄🙂.")


obj = Cesar_Cipher(alphabet)
# obj.code_text("hello", 3)
# obj.decode_text("khoor", 3)
obj.decode_text("khoor")
