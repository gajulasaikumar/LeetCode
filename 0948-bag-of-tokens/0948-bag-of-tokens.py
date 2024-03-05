class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i=0
        j=len(tokens)-1
        s=0
        m=0
        while i<=j:
            if tokens[i]<=power :
                s=s+1
                power-=tokens[i]
                i+=1
            else:
                if s>=1:
                    s=s-1
                    power+=tokens[j]
                j=j-1
            m=max(s,m)
        return m