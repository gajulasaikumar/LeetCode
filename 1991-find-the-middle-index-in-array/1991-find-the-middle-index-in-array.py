class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=nums[:i]
            y=nums[i+1:]
            if sum(x)==sum(y):
                return i
        return -1
            