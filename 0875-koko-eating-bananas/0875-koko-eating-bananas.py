class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def solve(n,arr):
            s=0
            for i in arr:
                s=s+math.ceil(i/n)
            return s
        i=1
        m=float("inf")
        j=max(piles)
        while i<=j:
            mid=(i+j)//2
            if solve(mid,piles)<=h:
                m=min(mid,m)
                j=mid-1
            elif solve(mid,piles)>h:
                i=mid+1
            print(solve(mid,piles),mid)
        return m