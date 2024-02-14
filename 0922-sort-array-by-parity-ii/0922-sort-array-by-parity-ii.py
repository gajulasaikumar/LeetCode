class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l=[]
        o=[]
        e=[]
        for i in nums:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        for i in range(len(o)):
            l.append(e[i])
            l.append(o[i])
        return l