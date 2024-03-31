class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        dp = [[0]*len(word2) for i in range(len(word1))]
        
        def helper(i, j):
            
            if i ==len(word1):
                return len(word2) - j
            elif j==len(word2):
                return len(word1) - i
            
            if dp[i][j]>0:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = helper(i+1, j+1)
                return dp[i][j]
            else:
                dp[i][j] = 1 + min(helper(i+1, j+1), helper(i+1, j), helper(i, j+1))
                return dp[i][j]
        
        
        return helper(0, 0)