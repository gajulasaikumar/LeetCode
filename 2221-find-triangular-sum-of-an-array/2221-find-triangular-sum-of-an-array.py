class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def solve(nums):
            l=[]
            for i in range(1,len(nums)):
                x=(nums[i-1]+nums[i])%10
                l.append(x)
            return l
        i=0
        n=len(nums)
        while i<n-1:
            x=solve(nums)
            nums=x
            i+=1
        return nums[0]