class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        def helper(i, j):
            
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return float("inf")
            
            if dp[i][j] > 0:
                return dp[i][j]
            
            right = grid[i][j] + helper(i, j+1)
            down = grid[i][j] + helper(i+1, j)
            
            # if reach end point, going down or right will be infinity
            if right == float("inf") and down == float("inf"):
                return grid[i][j]

            dp[i][j] = min(right, down)
            return dp[i][j]
        
        return helper(0,0)