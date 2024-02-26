class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s=0
        l=[]
        c=0
        for i in nums:
            s=s+i
            l.append(s)
        for i in range(len(nums)-1):
            if l[i]>=l[-1]-l[i]:
                c+=1
        return c