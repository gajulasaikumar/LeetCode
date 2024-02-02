class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        h=len(nums)-1
        l=0
        c=0
        nums.sort()
        while h>l:
            if nums[h]+nums[l]==k:
                c=c+1
                l=l+1
                h=h-1
            elif nums[h]+nums[l]<k:
                l=l+1
            else:
                h=h-1
                
            
        return c