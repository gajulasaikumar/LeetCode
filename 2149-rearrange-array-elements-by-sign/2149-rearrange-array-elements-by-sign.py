class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        x=[]
        l=[]
        y=[]
        for i in nums:
            if i<0:
                y.append(i)
            else:
                x.append(i)
        for i in range(len(x)):
            l.append(x[i])
            l.append(y[i])
        return l