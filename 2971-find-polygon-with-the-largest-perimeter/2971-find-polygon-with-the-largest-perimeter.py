class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
 
        nums.sort()
        s=0
        l=[]
        for i in nums:
            s=s+i
            l.append(s)
        m=-1
        for i in range(len(nums)-1):
            if l[i]>nums[i+1]:
                m=l[i+1]
        return m
                