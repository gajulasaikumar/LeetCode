class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        l=[]
        for i in nums:
            x=list(range(i[0],i[1]+1))
            l=l+x
        return len(set(l))