class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c=[[] for i in range(len(nums)+1)]
        d={}
        a=[]
        for i in nums:
            d[i]=1+d.get(i,0)
        for j in nums:
            c[d[j]].append(j)
        print(c)
        for i in c:
            i=sorted(i)[::-1]
            for k in i:
                a.append(k)
        return a