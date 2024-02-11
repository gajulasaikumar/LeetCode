class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        p=[]
        l=[]
        for i in range(len(matrix[0])):
            p=[]
            for j in range(len(matrix)):
                p.append(matrix[j][i])
            for j in range(len(matrix)):
                if matrix[j][i]==-1:
                    matrix[j][i]=max(p)
        return matrix
                