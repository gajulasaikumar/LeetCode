class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        l=[]
        r=""
        for i in order:
            if i in s:
                l.append(i*s.count(i))
        r="".join(l)
        for i in s:
            if i not in order:
                r=r+i
        return r