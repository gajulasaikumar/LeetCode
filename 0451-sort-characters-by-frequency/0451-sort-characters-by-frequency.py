class Solution:
    def frequencySort(self, s: str) -> str:
        c=[[] for i in range(len((s))+1)]
        d={}
        s1=""
        for i in s:
            d[i]=1+d.get(i,0)
        so = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(so)
        for i in so:
            s1=s1+(i[0]*i[1])
        return s1