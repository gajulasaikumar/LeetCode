class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        x=dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        p=list(x.keys())
        return p[:k]
    