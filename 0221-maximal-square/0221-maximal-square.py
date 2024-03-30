class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        self.dp = [[-1]*n for i in range(m)]
        
        self.ans = 0
        
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
                sq = sqrt(min(right, down_right, down))
                out = (1 + int(sq))**2
                                
                
            self.ans = max(self.ans, out)
            self.dp[i][j] = out
            return out
            
        for i in range(m):
            for j in range(n):
                helper(i,j)
        
        return self.ans
        