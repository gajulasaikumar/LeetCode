class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        x=text.split(" ")
        for i in x:
            for  j in i:
                if j in brokenLetters:
                    break
            else:
                c=c+1
        return c