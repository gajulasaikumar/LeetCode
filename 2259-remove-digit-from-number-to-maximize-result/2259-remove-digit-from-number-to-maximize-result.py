class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        m=-1
        
        l=[]
        for i in range(len(number)):
            if digit==number[i]:
                l.append(i)
        for i in l:
            s=number[:i]+number[i+1:]
            print(s)
            m=max(m,int(s))
        return str(m)