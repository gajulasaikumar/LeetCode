class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x=nums[i]|nums[j]
                v=bin(x)[2:]
                if v[-1]=='0':
                    return True
        return False