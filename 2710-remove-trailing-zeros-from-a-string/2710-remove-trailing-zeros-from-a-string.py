class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        x=int(num[::-1])
        return str(x)[::-1]