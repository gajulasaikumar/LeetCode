class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        for i in s:
            if ord(i)<58 and int(i) not in l:
                l.append(int(i))
        f=s=-1
        for i in l:
            if i>f:
                s=f
                f=i
            elif i>s and i!=f:
                s=i
        if s==-1:
            return -1
        return s
    
                
        