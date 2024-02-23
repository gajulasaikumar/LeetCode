class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        c=0
        c1=0
        print(d)
        for i in d:
            x=d[i]
            if x==2:
                c+=1
            else:
                if x%2==0:
                    c+=x//2
                else:
                    c+=x//2
                    c1+=1
        return [c,c1]