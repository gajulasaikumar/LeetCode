class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        a=1
        l=[]
        while len(l)<n:
            l.append(a)
            for i in l:
                if i+a==k and a!=i:
                    l.remove(a)
            a=a+1
        return sum(l)