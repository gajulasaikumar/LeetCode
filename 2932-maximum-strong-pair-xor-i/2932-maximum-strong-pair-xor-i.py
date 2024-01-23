class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        m=-1
        for i in nums:
            for j in nums:
                if abs(i-j)<=min(i,j):
                    m=max(m,i^j)
        return m