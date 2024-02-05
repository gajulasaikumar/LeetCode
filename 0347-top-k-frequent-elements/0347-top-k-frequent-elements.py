class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        x=dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        print(x)
        # s=sorted(d.values())
        # s.sort(key=lambda x: x[1], reverse=True)
        # print(s)
        x=list(x.keys())
        return x[:k]
    