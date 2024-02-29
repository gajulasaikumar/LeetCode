class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def solve(nums):
            s=1
            p=[]
            l=[]
            for i in nums:
                
                s*=i
                l.append(s)
                if s==0:
                    s=1
            s1=1
            for j in nums[::-1]:
                s1*=j
                p.append(s1)
                if s1==0:
                    s1=1
            return  max(max(l),max(p[::-1]))
        
        return solve(nums)