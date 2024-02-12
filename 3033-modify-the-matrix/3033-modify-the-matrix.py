class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix[0])):
            p=-1
            for j in range(len(matrix)):
                p=max(p,matrix[j][i])
            for j in range(len(matrix)):
                if matrix[j][i]==-1:
                    matrix[j][i]=p
        return matrix
                
