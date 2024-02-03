class Solution:
    def countKeyChanges(self, s: str) -> int:
        s1=""
        for i in s:
            if i.isupper():
                s1=s1+i.lower()
            else:
                s1=s1+i
        c=0
        p=s1[0]
        for k in s1:
            if p!=k:
                c=c+1
            p=k
    
            
        return c