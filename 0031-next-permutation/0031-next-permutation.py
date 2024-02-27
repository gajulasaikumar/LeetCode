class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        k=-1
        m=float("inf")
        for j in range(len(nums)-2,-1,-1):
            if nums[j]<nums[j+1]:
                k=j
                break
        if k==-1:
            nums[:]=nums[::-1]
            return
        for j in range(len(nums)-1,k,-1):
            if nums[j]>nums[k]:
                nums[k],nums[j]=nums[j],nums[k]
                break
        nums[k+1:]=nums[k+1:][::-1]
        
        
        
        