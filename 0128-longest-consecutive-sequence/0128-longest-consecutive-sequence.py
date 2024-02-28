class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        nums.sort()
        l=nums[0]
        c=1
        m=float("-inf")
        for i in range(1,len(nums)):
            if nums[i]-1 == l:
                c+=1
                l=nums[i]
            elif (nums[i])!=l:
                c=1
                l=nums[i]
            m=max(m,c)
        return m
                