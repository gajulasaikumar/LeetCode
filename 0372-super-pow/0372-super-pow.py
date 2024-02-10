class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        s=""
        for i in b:
            s=s+str(i)
        return pow(a,int(s),1337)