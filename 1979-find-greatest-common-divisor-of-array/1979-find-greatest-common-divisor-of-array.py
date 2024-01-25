class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x=min(nums)
        y=max(nums)
        m=-1
        i=1
        while i<=y:
            if x%i==0 and y%i==0:
                m=max(i,m)
            i=i+1
        return m