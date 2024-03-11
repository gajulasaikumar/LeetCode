class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c=0
        s=0
        d={0:1}
        for i in nums:
            s=s+i
            r=s%k
            if r in d:
                c=c+d[r]
            d[r]=d.get(r,0)+1
        return c
                