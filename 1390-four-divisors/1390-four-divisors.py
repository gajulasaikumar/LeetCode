class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def count(n):
            l=[]
            for i in range(1,int((n)**0.5)+1):
                if n%i==0:
                    l.append(i)
                    x=n//i
                    if x not in l: 
                        l.append(x)
            if len(l)==4:
                return sum(l)
            return 0
        s=0
        for k in nums:
            s=s+count(k)
        return s