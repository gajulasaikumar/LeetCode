class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        while j<len(t) and i<len(s):
            if t[j]==s[i]:
                j=j+1
            i=i+1
        return len(t)-j