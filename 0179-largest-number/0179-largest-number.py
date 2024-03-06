class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def solve(n,n1):
            return str(n)+str(n1)>str(n1)+str(n)
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if not solve(nums[j],nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        s=""
        for i in nums:
            s=s+str(i)
        return str(int(s))