class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        x=0
        m=float("inf")
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:       # left part sorted 
                x=nums[low]
                low=mid+1        
            else:        
                x=nums[mid]
                high=mid-1
            print(x)
            m=min(m,x)
        return m
                