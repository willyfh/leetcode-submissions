class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = n - 1
        x = m - 1
        y  = 0
        while (i<m and j>=0) or (x>=0 and y<n):
            
            if (i<m and j>=0 and matrix[i][j] == target) or (x>=0 and y<n and matrix[x][y] == target):
                return True
            else:
                if i<m and j>=0 and matrix[i][j] > target:
                    j-=1
                else:
                    i+=1
                if x>=0 and y<n and matrix[x][y] > target:    
                    x-=1
                else:
                    y+=1
            
        return False