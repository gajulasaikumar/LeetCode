class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                x=s[i:j]
                if x[::-1]==x:
                    l.append(x)
        p=[]
        for i in l:
            p.append(len(i)) 
        m=max(p)
        for i in l:
            if m==len(i):
                return i
        