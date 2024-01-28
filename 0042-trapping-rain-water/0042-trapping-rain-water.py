class Solution:
    def trap(self, height: List[int]) -> int:
        x=height
        q=x[::-1]
        i=x[0]
        j=q[0]
        y=0
        l=[]
        r=[]
        while y<len(x):
            if i<=x[y] :
                i=x[y]
            l.append(i)
            if j<=q[y]:
                j=q[y]
            r.append(j)
            y=y+1
        s=0
        r=r[::-1]
        for i in range(len(x)):
            s=s+min(r[i],l[i])-x[i]
        return s