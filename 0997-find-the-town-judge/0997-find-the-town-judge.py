class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l=[0]*(n+1)
        for i in trust:
            l[i[0]]-=1
            l[i[1]]+=1
        print(l)
        for k in range(1,n+1):
            if l[k]==n-1:
                return k
        return -1
            
        