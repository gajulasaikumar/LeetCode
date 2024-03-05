class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        nums=arr
        if nums[0]>nums[1]:
            return 0
        elif nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
        i=1
        j=len(nums)-2
        while i<=j:
            mid=(i+j)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif (nums[mid]>nums[mid-1]): 
                i=mid+1
            else:                           
                j=mid-1