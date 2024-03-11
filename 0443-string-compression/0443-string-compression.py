class Solution:
    def compress(self, chars: List[str]) -> int:
        def solve(x):
            v=x[0]
            c=1
            s=""
            for i in x[1:]:
                if v[-1]==i:
                    c=c+1
                else:
                    if c>1:
                        s=s+v[-1]+str(c)
                    else:
                        s=s+v[-1]
                    c=1
                    v=i
            if c>1:
                return (s+v+str(c))
            return s+v
        x=solve(chars)
        chars[:]=list(x)
        return len(list(x))