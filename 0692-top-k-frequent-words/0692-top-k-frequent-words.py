class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        x=[[] for i in range(len(words))]
        d={}
        l=[]
        for i in words:
            d[i]=1+d.get(i,0)
        for j in d:
            x[d[j]].append(j)
        print(d)
        print(x)
        for i in x[::-1]:
            for j in sorted(i):
                l.append(j)
        return (l[:k])
        