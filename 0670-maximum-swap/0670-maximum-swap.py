class Solution:
    def maximumSwap(self, num: int) -> int:
        m=[]
        x=list(str(num))
        for i in range(len(x)):
            for  j in range(len(x)):
                s=x[:]
                s[i],s[j]=s[j],s[i]
                s1="".join(s)
                m.append(int(s1))
        print(m)
        return int(max(m))

            