class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
        nums=a
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]<=nums[mid]:       # left part sorted 
                if nums[low]<=target and target<=nums[mid]:
                    high=mid-1             # remove right part
                else:
                    low=mid+1              # remove left part
                    
            else:                          # right part sorted
                if nums[mid]<=target and target<=nums[high]:
                    low=mid+1              # remove left part
                else:
                    high=mid-1             # remove right part
        return False
                
        