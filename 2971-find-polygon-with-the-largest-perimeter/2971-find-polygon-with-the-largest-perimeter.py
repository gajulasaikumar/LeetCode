class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
 
        nums.sort()
        l=[nums[0]]
        for i in nums[1:]:
            l.append(i+l[-1])
        print(l)
        m=-1
        for i in range(1,len(nums)-1):
            if l[i]>nums[i+1]:
                m=l[i+1]
        return m
                