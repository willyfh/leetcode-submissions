class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
     
        
        #reverse each row
        for i in range(m):
            k=0
            l = n-1
            while k < l:
                matrix[i][k], matrix[i][l] = matrix[i][l], matrix[i][k]
                k+=1
                l-=1