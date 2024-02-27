class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=[]
        c=0
        for i in nums:
            if i==0:
                l.append(c)
                c=0
            else:
                c+=1
        return max(l+[c])