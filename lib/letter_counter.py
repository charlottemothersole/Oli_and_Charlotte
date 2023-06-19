class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        # most_common_count = 1
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                # if char is not a letter, return false
                continue
            counter[char] = counter.get(char, 0) + 1 
            # set new key in counter as letter = if key doesnt exist use default val of 1
            # + 1 i.e. counter[a] = 2
            # 1: D: 1,    2: 
            if counter[char] > most_common_count:
                # if key value > current most_common_count
                most_common = char
                # most_common = current letter
                most_common_count = counter[char]
                # count = count + key value 
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
# counter = LetterCounter('aaaabbbba')
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]