class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        x=[]
        for i in range(1,rowIndex+2):
            y=[0]*i
            y[0]=1
            y[-1]=1
            x.append(y)
        print(x)
        for k in range(1,rowIndex+1):
            p=x[k-1]
            for i in range(len(x[k])):
                if x[k][i]==0:
                    x[k][i]=p[i-1]+p[i]
        return x[-1]
            