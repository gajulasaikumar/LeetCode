class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        for i in range(len(order)):
            d[order[i]]=i
        s1=(len(s)-1)*["0"]
        a=[]
        for j in range(len(s)):
            if s[j] in d:
                x=d[s[j]]
                s1[x]=s[j]*(s.count(s[j]))
            else:
                s1.append(s[j])
        return "".join(s1).replace("0","")