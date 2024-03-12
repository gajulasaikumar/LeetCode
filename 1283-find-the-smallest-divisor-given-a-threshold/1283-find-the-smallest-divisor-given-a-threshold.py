class Solution:
    import math
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def solve(arr,n):
            s=0
            for i in arr:
                s=s+math.ceil(i/n)
            return s
        i=1
        j=max(nums)
        m=float("inf")
        while i<=j:
            mid=(i+j)//2
            if solve(nums,mid)<=threshold:
                m=min(mid,m)
                j=mid-1
            else:
                i=mid+1
        return m
                
                