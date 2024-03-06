class Solution:
    def numSplits(self, s: str) -> int:
        d={}
        d1={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            d1[s[i]]=i
        x=list(d.values())+list(d1.values())
        x.sort()
        m=len(x)//2
        return x[m]-x[m-1]
        