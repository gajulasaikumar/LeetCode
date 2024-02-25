class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        m=min(nums)
        ma=max(nums)
        for i in set(nums):
            if i!=m and i!=ma:
                return i
        return -1