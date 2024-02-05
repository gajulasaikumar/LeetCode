class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        c=[[] for i in range(len(nums)+1)]
        for i in nums:
            d[i]=1+d.get(i,0)
        print(d)
        for i,j in d.items():
            c[j].append(i)
        print(c)
        p=[]
        for i in c[::-1]:
            for j in i:
                k=k-1
                p.append(j)
                if k==0:
                    return p
                
            
    