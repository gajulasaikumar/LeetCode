class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        a=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                a=mid
                high=mid-1
            else:
                low=mid+1
        low=0
        high=len(nums)-1
        a1=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                a1=mid
                high=mid-1
            else:
                low=mid+1
        if a==len(nums) or nums[a]!=target:
            return [-1,-1]
        return [a,a1-1]