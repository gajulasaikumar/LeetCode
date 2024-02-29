class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def solve(num):
            l=[]
            for i in range(1,int(num**(0.5))+1):
                if num%i==0:
                    l.append(i)
                    if num//i!=i:
                        l.append(num//i)
            return l
        l=[]
        s=set()
        for i in nums:
            l+=solve(i)
        for i in set(l):
            if i>1:
                for j in range(2,int(i**(0.5))+1):
                    if i%j==0:
                        break  
                else:
                    s.add(i)
        return len(s)