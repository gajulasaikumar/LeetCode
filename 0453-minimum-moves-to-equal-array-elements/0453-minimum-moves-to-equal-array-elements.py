class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s=0
        m=min(nums)
        for i in nums:
            s=s+i-m
        return s
        