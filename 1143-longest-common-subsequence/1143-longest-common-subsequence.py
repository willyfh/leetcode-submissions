class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = [[-1]*len(text2) for i in range(len(text1))]
        return self.helper(text1, text2, len(text1)-1, len(text2)-1)
    
    def helper(self, text1, text2, i, j):
        ans = 0
        if i<0 or j<0:
            return 0
        if self.dp[i][j] > -1:
            return self.dp[i][j]
        
        if text1[i] == text2[j]:
            
            ans = 1 + self.helper(text1, text2, i-1, j-1)
        else:
            ans = max(self.helper(text1, text2, i, j-1), self.helper(text1, text2, i-1, j))
            
        self.dp[i][j] = ans
            
        return ans
            