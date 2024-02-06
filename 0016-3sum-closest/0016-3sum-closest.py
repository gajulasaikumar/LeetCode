class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=nums
        nums.sort()
        an=sum(nums[:3])
        
        for a in range(len(nums)-2):
            k=nums[a]
            i=a+1
            j=len(nums)-1
            while j>i:
                s=k+nums[i]+nums[j]
                if abs(s - target) < abs(an - target):
                    an = s
                if s<target:
                    i=i+1
                else:
                    j=j-1
                
        return an