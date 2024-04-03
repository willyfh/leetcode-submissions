class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        # # Recursive
        dp = [[-1]*len(t) for i in range(len(s))]
        
        
        def helper(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if dp[i][j] > -1:
                return dp[i][j]
            out = 0
            if s[i] == t[j]:
                
                out = helper(i+1, j+1)
                
                out+= helper(i+1, j)
                
            else:
                out = helper(i+1, j)
            
            dp[i][j] = out
            return out
            
        return helper(0, 0)

#         ## ITERATIVE
    
#         dp = [[0]*len(t) for i in range(len(s)+1)]
        
#         i = 0
#         j = 0
        
        
        