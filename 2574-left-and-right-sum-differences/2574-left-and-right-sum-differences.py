class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s=0
        l=[]
        for i in nums:
            l.append(s)
            s=s+i
        p=[]
        k=0
        for i in nums[::-1]:
            p.append(k)
            k=k+i
        print(p)
        print(l)
        k=k+i
        r=[]
        p=p[::-1]
        for i in range(len(nums)):
            r.append(abs(l[i]-p[i]))
        return r