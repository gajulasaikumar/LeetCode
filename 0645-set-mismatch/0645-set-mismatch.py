class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x=set(list(nums))
        n=len(nums)
        r=((n*(n+1))//2-sum(x))
        for i in set(nums):
            if nums.count(i)>1:
                return [i,r]