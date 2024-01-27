class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l=[]
        p=[]
        for i in range(len(s)):
            l.append(s.index(s[i]))
            p.append(t.index(t[i]))
        return l==p
            
        