class Solution:
    def smallestNumber(self, num: int) -> int:
        
        num=str(num)
        if "-" in num:
            return (-1)*int("".join(sorted(num[1:])[::-1]))
        x=sorted(num)
        if "0" in x:
            num="".join(x)
            x=num.count("0")
            
            num=num.replace("0","")
            n=""
            n=num[:1]+"0"*x+num[1:]
            print(n)
            return int("".join(n))
        return int("".join(x))
                