class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        l=[9,9,8,7,6,5,4,3,2,1]
        x=1
        p=[]
        s=1
        for i in l:
            x=x*i
            p.append(x+s) 
            s=s+x
        print(p)
        return p[n-1]