class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i%space]+=1
        m=max(d.values())
        l=[]
        for i in nums:
            if d[i%space]>=m:
                l.append(i)
        print(l)
        return min(l)