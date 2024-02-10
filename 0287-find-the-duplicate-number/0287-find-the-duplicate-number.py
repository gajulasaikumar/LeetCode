class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        for k in d:
            if d[k]>1:
                return k