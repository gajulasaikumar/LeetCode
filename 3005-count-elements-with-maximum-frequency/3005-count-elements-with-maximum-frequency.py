class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=0
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        m=max(d.values())
        for i in d:
            if d[i]==m:
                c=c+m
        return c