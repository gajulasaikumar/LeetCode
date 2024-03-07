class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m=max(nums)
        s=0
        for i in range(k):
            s=s+m
            m=m+1
        return s


        