class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
#         # recursive + memoization
#         dp = [[0]*len(s) for i in range(len(s))]
#         def helper(i, j):
#             if i==j:
#                 return 1
#             if i>j:
#                 return 0
            
#             if dp[i][j]>0:
#                 return dp[i][j]
#             if s[i] == s[j]:
#                 dp[i][j] = 2 + helper(i+1, j-1)
#                 return dp[i][j]
#             else:
#                 dp[i][j] = max(helper(i+1, j), helper(i, j-1))
#                 return dp[i][j]
            
#         return helper(0, len(s)-1)   
        
        # iterative
        dp = [[0]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            
        for j in range(len(s)):
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][-1]
                
    