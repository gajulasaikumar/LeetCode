class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s1=[]
        t=order
        for i in s:
            if i not in t:
                s1.append(i)
        l=[]
        for j in range(len(t)):
            if t[j] in s:
                l.append(t[j]*s.count(t[j]))
        return "".join(l+s1)