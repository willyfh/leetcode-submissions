class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        curr_row = [0]*n
        next_row = matrix[-1]
        for i in range(n-2, -1, -1):
            for j in range(n):
                if j == 0:
                    curr_row[j] = matrix[i][j] + min(next_row[j], next_row[j+1])
                elif j==n-1:
                    curr_row[j] = matrix[i][j] + min(next_row[j], next_row[j-1])
                else:
                    curr_row[j] = matrix[i][j] + min(next_row[j], next_row[j-1], next_row[j+1])
            next_row, curr_row = curr_row, next_row
        return min(next_row)