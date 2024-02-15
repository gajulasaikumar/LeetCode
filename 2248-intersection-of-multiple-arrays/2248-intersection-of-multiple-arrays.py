class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        d={}
        l=[]
        for i in nums:
            l=l+i
        for i in l:
            d[i]=1+d.get(i,0)
        ans=[]
        for i in d:
            if d[i]%n==0:
                ans.append(i)
        return sorted(ans)