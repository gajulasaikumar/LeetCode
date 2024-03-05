class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[len(nums)-1]!=nums[len(nums)-2]:
            return nums[len(nums)-1]
        i=1
        j=len(nums)-2
        while i<=j:
            mid=(i+j)//2
            if nums[mid-1]!=nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif (mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid]==nums[mid+1]): #left
                i=mid+1
            else:                            #right
                j=mid-1
            
        