class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        l=[]
        for i in nums:
            d[i]=1+d.get(i,0)
        for i in d:
            if d[i]>len(nums)//2:
                return i