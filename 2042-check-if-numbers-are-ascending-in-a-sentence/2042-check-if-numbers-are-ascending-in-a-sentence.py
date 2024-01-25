class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=[]
        s1=""
        for i in s:
            if i.isdigit():
                s1=s1+i
            else:
                if s1!="":
                    l.append(int(s1))
                    s1=""
        if s1.isdigit():
            l.append(int(s1))
        print(l)
        print(sorted(list(set(l))))
        return sorted(list(set(l)))==l
            