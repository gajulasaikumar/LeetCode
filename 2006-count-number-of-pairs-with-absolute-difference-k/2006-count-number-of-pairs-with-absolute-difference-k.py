class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i<j and abs(nums[i]-nums[j])==k:
                    c=c+1
        return c