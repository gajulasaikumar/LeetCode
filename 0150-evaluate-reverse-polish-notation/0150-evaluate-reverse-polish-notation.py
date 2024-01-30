class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        p=[]
        for i in tokens:
            if i not in"*+/-":
                p.append(int(i))
            else:
                a=p[-2]
                b=p[-1]
                if i=="+":
                    v=a+b
                elif i=="-":
                    v=a-b
                elif i=="*":
                    v=a*b
                else:
                    v=int(a/b)
                p.pop()
                p.pop()
                p.append(v)
        return p[0]

        