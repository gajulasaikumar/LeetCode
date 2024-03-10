class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        s=[]
        k=0
        re=[]
        for i in words:
            if i!=-1:
                k=0
                s.append(i)
            else:
                k=k+1
                if k>len(s):
                    re.append(-1)
                else:
                    re.append(s[::-1][k-1])
        return re
            