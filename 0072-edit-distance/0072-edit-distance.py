class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        self.dp = [[-1]*n for x in range(m)]
        
        def helper(i, j):
            
            if i==m and j==n:
                return 0
            elif i==m:
                return n-j
            elif j==n:
                return m-i
            
            if self.dp[i][j] >=0:
                return self.dp[i][j]
            
            if word1[i] == word2[j]:
                self.dp[i][j] = helper(i+1, j+1)
                return self.dp[i][j]
            else:
                
                delete = 1 + helper(i+1, j)
                replace = 1 + helper(i+1, j+1)
                insert = 1 + helper(i, j+1)
                
                self.dp[i][j] = min(delete, replace, insert)
                return self.dp[i][j]
            
        return helper(0, 0)