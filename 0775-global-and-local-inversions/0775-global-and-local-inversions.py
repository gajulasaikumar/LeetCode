class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n=len(nums)
        for i,j in enumerate(nums):
            if abs(i-j)>1:
                return False
        return True