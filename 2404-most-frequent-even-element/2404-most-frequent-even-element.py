class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i%2==0:
                d[i]=1+d.get(i,0)
        print(d)
        if d=={}:
            return -1
        m=max(d.values())
        l=[]
        for i in d:
            if d[i]==m:
                l.append(i)
 
        return min(l)