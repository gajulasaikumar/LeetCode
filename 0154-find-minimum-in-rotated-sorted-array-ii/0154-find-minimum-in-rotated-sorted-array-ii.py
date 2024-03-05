class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        low=0
        x=0
        m=nums[0]
        high=len(nums)-1
        while low<=high:
            if nums[low] < nums[high]: 
                return min(m, nums[low])
            mid=(low+high)//2
            m=min(m,nums[mid])
            if nums[mid]==nums[high]==nums[low]:
                high-=1
            elif nums[low]<=nums[mid]:   
                low=mid+1        
            else:        
                high=mid-1
            
        return m
                