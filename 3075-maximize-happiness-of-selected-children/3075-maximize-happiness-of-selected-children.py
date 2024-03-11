class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        x=0
        c=0
        m=-1
        happiness.sort(reverse=True)
        for i in range(k):
            if happiness[i]<=0:
                x=x+0
                c=0
            else:
                x=x+happiness[i]-c
            c=c+1
            m=max(x,m)
        return m
