class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        for i in d:
            if d[i]==n:
                return i
        