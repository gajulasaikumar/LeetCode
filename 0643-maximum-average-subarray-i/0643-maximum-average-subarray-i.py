class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m=s=sum(nums[:k])
        for i in range(k,len(nums)):
            s=s+nums[i]-nums[i-k]
            print(s)
            m=max(s,m)
        return m/k
            