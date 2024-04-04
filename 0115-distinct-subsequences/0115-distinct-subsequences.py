class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
#         # Recursive
#         dp = [[-1]*len(t) for i in range(len(s))]
        
        
#         def helper(i, j):
#             if j == len(t):
#                 return 1
#             if i == len(s):
#                 return 0
#             if dp[i][j] > -1:
#                 return dp[i][j]
#             out = 0
#             if s[i] == t[j]:
                
#                 out = helper(i+1, j+1)
                
#                 out+= helper(i+1, j)
                
#             else:
#                 out = helper(i+1, j)
            
#             dp[i][j] = out
#             return out
            
#         return helper(0, 0)

        ## ITERATIVE
    
        dp = [[0]*(len(t)+1) for i in range(len(s)+1)]
            
        for i in range(len(s)+1):
            dp[i][-1] = 1
        

        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                    
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]
        
        