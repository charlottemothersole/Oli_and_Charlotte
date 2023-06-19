# class VowelRemover:
#     def __init__(self, text):
#         self.text = text
#         self.vowels = ["a", "e", "i", "o", "u"]

#     def remove_vowels(self):
#         i = 0
#         new_text = self.text
#         while i < len(self.text):
#             if self.text[i].lower() in self.vowels:
#                 print('i',i)
#                 print('self.text',self.text)
#                 print('self.text[i]',self.text[i])
#                 # 'ab'
#                 # 'aeiou'
#                 # self.text = self.text[:i] + self.text[i+1:]
#                 new_text = self.text.replace(self.text[i], '')
#                 # aeiou = 0:0 + 1:end = iou
#                 # 
#                 # print('i',i)
#                 # print('self.text[:i]', self.text[:i])
#                 # print('self.text[i:]', self.text[i+1:])
#                 # print('self.text[:i] + self.text[i:]', self.text[:i] + self.text[i+1:])
#                 print('new_text',new_text)
#                 # b, a,
#                 # eiou, eou, eo
#             i += 1
#             self.text = new_text
#         return self.text
    


class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]
# iterate over the characters of the text
# for each character, check if it is in vowel list
# if true, slice from i+1 to end of string 
# e.g. text = 'aeiou' text[i+]
# if not, increase counter (i)

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else :
                i += 1
        return self.text

new = VowelRemover('aeiou')
print(new.remove_vowels())
