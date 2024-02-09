class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        s1=[]
        t=order
        for i in s:
            if i not in t:
                s1.append(i)
        print(s1)
        a=[]
        l=[]
        for j in range(len(t)):
            if t[j] in s:
                l.append(t[j]*s.count(t[j]))
        print(l,s1)
        return "".join(l+s1)