class Solution:
    def climbStairs(self, n: int) -> int:
        f1=1
        f2=2
        for i in range(2,n):
            n=f1+f2
            f1=f2
            f2=n
        return n