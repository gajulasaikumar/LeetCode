class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a=len(nums)
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]>=target:
                a=mid
                j=mid-1
            else:
                i=mid+1
        return a