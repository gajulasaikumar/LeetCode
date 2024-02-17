class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c=0
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        print(d)
        for i in d:
            if i-1 in d:
                c=max(d[i]+d[i-1],c)
        return c