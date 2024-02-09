class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    l.append([i,j])
        print(l)
        for i in l:
            matrix[i[0]]=[0]*len(matrix[0])
            for k in range(len(matrix)):
                matrix[k][i[1]]=0

        
        