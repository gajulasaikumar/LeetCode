class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num=[]
        for i in nums:
            num.append(i**2)
        l=[]
        i=0
        j=len(nums)-1
        while j>=i:
            if num[j]>num[i]:
                l.append(num[j])
                j=j-1
            else:
                l.append(num[i])
                i=i+1
        return l[::-1]