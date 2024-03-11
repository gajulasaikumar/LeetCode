class Solution:
    def countAndSay(self, n: int) -> str:
        def solve(x):
            v=x[0]
            c=1
            s=""
            for i in x[1:]:
                if v[-1]==i:
                    c=c+1
                else:
               
                    s=s+str(c)+v[-1]
                    c=1
                    v=i
            return (s+str(c)+v)
        s="1"
        for i in range(1,n):
            s=(solve(s))
        return s
                    
                