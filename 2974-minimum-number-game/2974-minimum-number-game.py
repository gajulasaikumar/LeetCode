class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        j=1
        while i<len(nums) and j<len(nums):
            nums[i],nums[j]=nums[j],nums[i]
            j=j+2
            i=i+2
        return nums
            
        