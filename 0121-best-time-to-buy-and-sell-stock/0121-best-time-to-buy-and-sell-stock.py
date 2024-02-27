class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=float("inf")
        ma=0
        for i in prices:
            m=min(i,m)
            ma=max(ma,i-m)
        return ma