class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s=0
        l=[]
        p=[]
        c=0
        for i in nums[::-1]:
            s=s+i
            l.append(s)
        s1=0
        for i in nums:
            s1=s1+i
            p.append(s1)
        l=l[::-1]
        for i in range(len(nums)-1):
            if p[i]>=l[i+1]:
                c+=1
        return c