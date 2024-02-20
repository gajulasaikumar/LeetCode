
import sys
sys.set_int_max_str_digits(10**6)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        c=""
        l=[]
        for i in  num:
            c=c+str(i)
        v=str((int(c)+k))
        for k in v:
            l.append(int(k))
        return l
        