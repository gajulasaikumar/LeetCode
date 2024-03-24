class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r=[]
        for i in range(2**len(nums)):
            l=[]
            for j in range(len(nums)):
                if (i&(1<<j))!=0:
                    l.append(nums[j])
            r.append(l)
        return r
                