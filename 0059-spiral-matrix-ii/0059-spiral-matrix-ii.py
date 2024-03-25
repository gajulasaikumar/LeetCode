class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m=[[0] *n for i in range(n)]
        rs=0
        cs=0
        rl=n-1
        cl=n-1
        j=1
        while j<= n*n:
            for i in range(cs,cl+1):
                m[rs][i]=j
                j+=1
            rs+=1
            for i in range(rs,rl+1):
                m[i][cl]=j
                j+=1
            cl-=1
            for i in range(cl,cs-1,-1):
                m[rl][i]=j
                j+=1
            rl-=1
            for i in range(rl,rs-1,-1):
                m[i][cs]=j
                j+=1
            cs+=1
            print(m)
        return m