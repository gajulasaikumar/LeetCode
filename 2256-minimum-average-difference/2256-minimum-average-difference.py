class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        s=0
        p=[]
        l=[]
        for i in nums:
            s=s+i
            l.append(s)
        s1=0
        for j in nums[::-1]:
            
            p.append(s1)
            s1+=j
        p=p[::-1]
        print(p,l)
        n=len(nums)
        m=float("inf")
        j=0
        for i in range(n):
            if (n-(i+1)) ==0:
                x=(l[i]//(i+1))
            else:
                x=abs(l[i]//(i+1) - p[i]//(n-(i+1)))
            if x<m:
                j=i
                m=x
        return j