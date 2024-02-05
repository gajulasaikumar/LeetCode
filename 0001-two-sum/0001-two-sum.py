class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=nums
        d={}
        for i in range(len(x)):
            diff=target-x[i]
            if diff in d:
                return [d[diff],i]
            d[x[i]]=i
            
        