class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            x=nums[:i+1]
            y=nums[i+1:]
            l.append(len(set(x))-len(set(y)))
        return l