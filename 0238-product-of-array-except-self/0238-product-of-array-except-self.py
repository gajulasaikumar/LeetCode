class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        p=1
        for i in range(len(nums)):
            l.append(p)
            p*=nums[i]
        print(l)
        p1=1
        r=[]
        for i in range(len(nums)-1,-1,-1):
            r.append(p1)
            p1*=nums[i]
        print(r[::-1])
        r=r[::-1]
        x=[0]*len(nums)
        for i in range(len(l)):
            x[i]=l[i]*r[i]
        return x
            