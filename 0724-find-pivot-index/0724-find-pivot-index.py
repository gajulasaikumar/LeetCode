class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r=sum(nums)
        l=0
        for i in range(len(nums)):
            l=l+nums[i]
            if  l==r:
                return i
            r=r-nums[i]
        return -1