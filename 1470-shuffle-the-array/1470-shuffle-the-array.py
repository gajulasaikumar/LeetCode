class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        x=len(nums)//2
        n2=nums[:x]
        n1=nums[x:]
        print(n2,n1)
        for i,j in zip(n2,n1):
            l.append(i)
            l.append(j)
        return l
        