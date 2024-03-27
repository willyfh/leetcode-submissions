class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        @cache
        def helper(i, j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j==n-1:
                return 1
            
            return helper(i+1, j)+ helper(i, j+1)
        
        return helper(0,0)