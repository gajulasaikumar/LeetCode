class Solution:
    def largestInteger(self, num: int) -> int:
        a=list(str(num))
        x=[]
        y=[]
        for i in a:
            if int(i)%2==0:
                x.append(i)
            else:
                y.append(i)
        x.sort()
        y.sort()
        z=[]
        for i in range(len(a)):
            if int(a[i])%2==0:
                z.append(x.pop())
            else:
                z.append(y.pop())
        return int("".join(z))