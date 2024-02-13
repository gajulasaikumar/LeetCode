class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x=nums[0]
        l=[x]
        for i in nums[1:]:
            x=x+i
            l.append(x)
        return l