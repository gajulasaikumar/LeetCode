class Solution:
    import math
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def solve(n,arr):
            s=0
            for i in arr:
                s=s+(i//n)
            return s
        i=1
        m=float("inf")
        j=max(candies)
        if sum(candies)<k:
            return 0
        while i<=j:
            mid=(i+j)//2
            if solve(mid,candies)<k:
                j=mid-1
            elif solve(mid,candies)>=k:
                i=mid+1
                m=mid

        return m