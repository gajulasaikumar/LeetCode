class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=num**(1/2)
        return int(x)==x
        