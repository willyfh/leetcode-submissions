class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        self.dp = [[-1]*n for i in range(m)]
        
        ans = 0
        def helper(i, j):
        
            if i ==m or j == n:
                return 0
            if self.dp[i][j] != -1:
                return self.dp[i][j]
            out = 0
            if matrix[i][j] == "1":
                right = helper(i, j+1)
                down_right = helper(i+1,j+1)
                down = helper(i+1, j)
                out = 1 + min(right, down_right, down)
                                
                
            self.dp[i][j] = out
            return out
            
        for i in range(m):
            for j in range(n):
                out = helper(i,j)
                ans = max(ans, out)
        
        return ans*ans