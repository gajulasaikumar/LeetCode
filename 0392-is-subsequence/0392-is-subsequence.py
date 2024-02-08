class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        j=len(t)-1
        l1=0
        v=0
        j1=len(s)-1
        while j>=l and j1>=l1:
            if t[j]==s[j1]:
                v=v+1
                j=j-1
                j1=j1-1
            elif s[l1]==t[l]:
                l1=l1+1
                l=l+1
                v=v+1
            elif s[l1]!=t[l]:
                l=l+1
            elif s[j1]!=t[j]:
                j=j-1
        return v==len(s)
                
                