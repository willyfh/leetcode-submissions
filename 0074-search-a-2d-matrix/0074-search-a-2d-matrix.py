class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        t = m*n
        
        left = 0
        right = t-1
        

        while left <= right:
            
            mid = (left + right) // 2
            
            i = mid // n
            j = mid % n
            
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False