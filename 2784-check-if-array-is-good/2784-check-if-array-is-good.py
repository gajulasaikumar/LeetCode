class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=max(nums)
        if nums.count(m)==2 and len(nums)==m+1:
            s=(m*(m+1))//2
            return s+m==sum(nums)
        return False
         