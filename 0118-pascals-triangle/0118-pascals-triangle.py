class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(1,numRows+1):
            x=[0]*i
            x[0]=1
            x[-1]=1
            l.append(x)
        for i in range(1,numRows):
            y=l[i-1]
            for j in range(len(l[i])):
                if l[i][j]==0:
                    l[i][j]=y[j-1]+y[j]
        return l