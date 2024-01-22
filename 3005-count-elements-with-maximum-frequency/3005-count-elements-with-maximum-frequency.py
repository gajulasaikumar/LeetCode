class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=0
        m=-1
        for i in set(nums):
            m=max(m,nums.count(i))
        for i in set(nums):
            if m==nums.count(i):
                c=c+m
        return c