class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=[]
        b=[]
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                b.append(i)
        for j in a:
            if j not in b:
                return j