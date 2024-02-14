class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        x=[]
        l=[]
        y=[]
        for i in range(len(nums)):
            if i%2==0:
                y.append(nums[i])
            else:
                x.append(nums[i])
        y.sort(reverse=True)
        x.sort()
        print(x)
        for i in range(len(nums)):
            if i%2==0:
                l.append(y.pop())
            else:
                l.append(x.pop())
        return l