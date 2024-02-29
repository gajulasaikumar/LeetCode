class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def solve(nums):
            if nums==[]:
                return 0
            s=1
            p=[]
            l=[]
            for i in nums:
                s*=i
                l.append(s)
            s1=1
            for j in nums[::-1]:
                s1*=j
                p.append(s1)
            return  max(max(l),max(p[::-1]))
        l=[]
        p=[]
        for i in nums:
            if i!=0:
                p.append(i)
            else:
                l.append(p)
                p=[]
        if p!=[]:
            l.append(p)
        m=float("-inf")
        for i in l:
            x=solve(i)
            m=max(x,m)
        if 0 in nums and m<0:
            return 0
        return m