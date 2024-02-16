class Solution:
    def pivotInteger(self, n: int) -> int:
        a=0
        b=(n*(n+1))//2
        for i in range(1,n+1):
            a=a+i
            if a==b:
                return i
            b=b-i
        return -1