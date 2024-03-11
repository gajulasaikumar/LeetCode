class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s=0
        d={0:1}
        c=0
        for i in nums:
            s=s+i
            di=s-k
            if di in d:
                c+=d[di]
            d[s]=d.get(s,0)+1
        return c
            
    