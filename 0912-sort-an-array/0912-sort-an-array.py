class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        def merge(nums,low,mid,high):
            left=low
            n=[]
            right=mid+1
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    n.append(nums[left])
                    left+=1
                else:
                    n.append(nums[right])
                    right+=1
            while left<=mid:
                n.append(nums[left])
                left+=1
            while right<=high:
                n.append(nums[right])
                right+=1
            for i in range(low,high+1):
                nums[i]=n[i-low]
            
        def mergesort(nums,low,high):
            if low>=high:
                return
            mid=(low+high)//2
            mergesort(nums,low,mid)
            mergesort(nums,mid+1,high)
            merge(nums,low,mid,high)
            return nums
        x=mergesort(nums,0,len(nums)-1)
        return x
        
            