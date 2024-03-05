class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        for i in s:
            if ord(i)<58 and int(i) not in l:
                l.append(int(i))
        l.sort()
        if len(l)<2:
            return -1
        return l[-2]
        