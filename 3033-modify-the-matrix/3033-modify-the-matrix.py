class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        p=[]
        l=[]
        for i in range(len(matrix[0])):
            p=[]
            for j in range(len(matrix)):
                p.append(matrix[j][i])
            l.append(max(p))
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i]==-1:
                    matrix[j][i]=l[i]
        return matrix
                