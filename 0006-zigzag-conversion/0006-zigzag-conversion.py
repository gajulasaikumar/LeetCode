class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        a=[]
        l=""
        x1=numRows-2
        i=0
        while i<len(s):
            l=[0]*numRows
            p=[0]*numRows
            x=s[i:i+numRows]
            y=s[i+numRows:i+numRows+x1]
            for i1 in range(len(x)):
                l[i1]=x[i1]
            k=0
            for j in range(numRows-2,0,-1):
                if k<len(y):
                    p[j]=y[k]
                    k=k+1
            i+=numRows+x1
            a.append(l)
            a.append(p)
        n=""
        for i in range(numRows):
            s=""
            for j in  a:
                if j[i]!=0:
                    s=s+j[i]
            n=n+s
        return n
                
            
                