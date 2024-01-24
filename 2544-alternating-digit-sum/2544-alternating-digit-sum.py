class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n=str(n)
        s=0
        for i in range(len(n)):
            if i%2==0:
                s=s+int(n[i])
            else:
                s=s-int(n[i])
        return s