class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d={}
        d1={}
        c=0
        l=[]
        for i in words1:
            if i in words2:
                l.append(i)
        for i in words1:
            d[i]=1+d.get(i,0)
        for j in words2:
            d1[j]=1+d1.get(j,0)
        print(d,d1)
        for i in l:
            if d1[i]==d[i]==1:
                c=c+1
        return c