class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=[]
        rs=0
        cs=0
        n=len(matrix)
        n1=len(matrix[0])
        r=len(matrix)-1
        c=len(matrix[0])-1
        j=0
        while j<n1*n:
            #top row
            for i in range(cs,c+1):
                l.append(matrix[rs][i])
                j+=1
            rs+=1
            if j==n*n1:
                break
            
            for i in range(rs,r+1):
                
                l.append(matrix[i][c])
                j+=1
            c-=1
            if j==n*n1:
                break
        
            for i in range(c,cs-1,-1):
                l.append(matrix[r][i])
                j+=1
          
            r-=1
            if j==n*n1:
                break
            
            for i in range(r,rs-1,-1):
                l.append(matrix[i][cs])
                j+=1
            cs+=1
           
        return l
