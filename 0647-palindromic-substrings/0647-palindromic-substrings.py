class Solution:
    def countSubstrings(self, s: str) -> int:
        n=""
        c=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                x=s[i:j]
                if x==x[::-1]:
                    c=c+1
        return c
                
            