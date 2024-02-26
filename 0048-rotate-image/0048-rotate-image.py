class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res=[]
        for i in range(len(matrix[0])):
            l=[]
            for j in range(len(matrix)):
                l.append(matrix[j][i])
            res.append(l[::-1])
        matrix[:]=res
        
        