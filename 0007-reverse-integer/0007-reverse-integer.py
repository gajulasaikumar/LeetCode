class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x[0]=='-':
            y=x[1::]
            if int('-'+ y[::-1])<-2147483648:
                return 0
            else:
                return int('-'+ y[::-1])
        elif int(x[::-1])>2147483647:
            return 0
        else:
            return int(x[::-1])