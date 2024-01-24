class Solution:
    def minimumSum(self, num: int) -> int:
        x=str(num)
        l=sorted(list(x))
        return int(l[0]+l[3])+int(l[1]+l[2])