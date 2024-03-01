class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x=s.count("1")
        if x==1:
            x=s.replace("1","")
            return x+"1"
        k=""
        for i in s:
            if i!="1":
                k=k+i
        return "1"*(x-1)+k+"1"