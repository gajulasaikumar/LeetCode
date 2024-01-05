class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=nums
        for i in range(len(x)):
            diff=target-x[i]
            for j in range(i+1,len(x)):
                if diff==x[j]:
                    return [i,j] 
        