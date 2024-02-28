class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        n=set(nums)
        m=-1
        c=0
        for i in n:
            if i-1 not in n:
                x=i-1
                c=0
                x=x+1
                while x in n:
                    x=x+1
                    c+=1
                m=max(c,m)
        return m