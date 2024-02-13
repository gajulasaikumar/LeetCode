class Solution:
    def isUgly(self, n: int) -> bool:
        def solve(n):
            if n==0:
                return False
            if n==1:
                return True
            if n%2==0:
                return solve(n//2)
            if n%5==0:
                return solve(n//5)
            if n%3==0:
                return solve(n//3)
        return solve(n)