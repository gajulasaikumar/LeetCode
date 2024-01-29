class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        l=[]
        m=-1
        s=0
        for i in range(len(nums)):
            m=max(nums[i],m)
            s=s+m+nums[i]
            l.append(s)
        return l
        
        