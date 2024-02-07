class Solution:
    def frequencySort(self, s: str) -> str:
        c=[[] for i in range(len((s))+1)]
        d={}
        for i in s:
            d[i]=1+d.get(i,0)
        for j in d:
            c[d[j]].append(j)
        s1=""
        for i in c[::-1]:
            for j in i:
                s1=s1+j*d[j]
        return s1