class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        l=[]
        s=s1+" "+s2
        s=s.split(" ")
        d={}
        for i in s:
            d[i]=1+d.get(i,0)
        for i in d:
            if d[i]==1:
                l.append(i)
        return l
        