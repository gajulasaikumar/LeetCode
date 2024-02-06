class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=set()
        nums.sort()
        for a in range(len(nums)):
            k=nums[a]
            i=a+1
            j=len(nums)-1
            while j>i:
                s=k+nums[i]+nums[j]
                if s<0:
                    i=i+1
                elif s>0:
                    j=j-1
                else:
                    l.add((k,nums[i],nums[j]))
                    i=i+1
        return l