class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
 
        nums.sort()
        l=[]
        s=nums[0]
        for i in nums[1:]:
            l.append(s)
            s=s+i
        l.append(s)
        m=-1
        for i in range(len(nums)-1):
            if l[i]>nums[i+1]:
                m=l[i+1]
        return m
                