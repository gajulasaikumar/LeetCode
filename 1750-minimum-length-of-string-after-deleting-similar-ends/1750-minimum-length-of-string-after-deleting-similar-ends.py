class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        while i<j and s[i]==s[j]:
            b=s[i]
            while i<=j and s[i]==b:
                i+=1
            while i<j and s[j]==b:
                j=j-1
            
            
        x=j-i+1
        return x
        