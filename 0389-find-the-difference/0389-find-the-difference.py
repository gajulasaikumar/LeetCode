class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in t:
            d[i]=1+d.get(i,0)
        print(d)
        k=""
        for j in s:
            if j in d:
                d[j]-=1
        print(d)
        k=""
        for i in d:
            if d[i]>=1:
                k=k+i
        return k