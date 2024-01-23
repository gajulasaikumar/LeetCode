class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        l=[]
        for i in nums[::-1]:
            l.append(i)
            c=0
            for i in range(1,k+1):
                if i in l:
                    c=c+1
            if c==k:
                return len(l)