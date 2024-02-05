class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=[]
        b=[]
        for i in s:
            if i not in a:
                a.append(i)
            else:
                b.append(i)
        for j in a:
            if j not in b:
                return s.index(j)
        return -1


        