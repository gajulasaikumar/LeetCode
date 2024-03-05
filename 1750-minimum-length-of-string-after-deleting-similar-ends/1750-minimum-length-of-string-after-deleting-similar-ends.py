class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        while i<j and s[i]==s[j]:
            while i+1<j and s[i]==s[i+1]:
            
                i+=1
            while i<j-1 and s[j]==s[j-1]:
         
                j=j-1
            i+=1
            j=j-1  
        x=j-i+1
        return x
        