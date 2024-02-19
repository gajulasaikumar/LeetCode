class Solution:
    def binaryGap(self, n: int) -> int:
        c=bin(n)[2:]
        l=[]
        for i in range(len(c)):
            if c[i]=="1":
                l.append(i)
        x=l[0]
        m=0
        for k in l[1:]:
            m=max(k-x,m)
            x=k
        return m
            
            