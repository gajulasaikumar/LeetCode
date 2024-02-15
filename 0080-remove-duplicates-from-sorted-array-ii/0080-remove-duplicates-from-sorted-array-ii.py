class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        l=[]
        for i in nums:
            d[i]=1+d.get(i,0)
        for i in d:
            if d[i]>=2:
                l=l+[i]*2
            else:
                l=l+[i]
        nums[:]=l