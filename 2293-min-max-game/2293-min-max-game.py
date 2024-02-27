class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def solve(nums):
            m=float("inf")
            ma=float("-inf")
            l=[]
            c=0
            for i in range(0,len(nums),2):
                if c==0:
                    m=min(nums[i+1],nums[i])
                    l.append(m)
                    c=c+1
                else:
                    ma=max(nums[i+1],nums[i])
                    l.append(ma)
                    c=c-1
            return l
        while len(nums)!=1:
            x=solve(nums)
            nums=x
        return nums[0]