class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        m=float("-inf")
        d={}
        for i in dimensions:
            x=((i[0]**(2))+(i[1]**2))**(1/2)
            m=max(x,m)
        l=[]
        for i in dimensions:
            x=((i[0]**(2))+(i[1]**2))**(1/2)
            if m==x:
                l.append(i[0]*i[1])
        return max(l)
            
            