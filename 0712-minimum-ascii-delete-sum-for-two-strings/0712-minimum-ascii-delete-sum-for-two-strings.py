class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        
        ## RECURSIVE
#         dp = [[-1]*len(s2) for i in range(len(s1))]
        
#         def helper(i, j):
#             if i == len(s1):
#                 s = 0
#                 for k in s2[j:]:
#                     s+=ord(k)
#                 return s
#             elif j==len(s2):
#                 s = 0
#                 for k in s1[i:]:
#                     s+=ord(k)
#                 return s
#             if dp[i][j] >-1:
#                 return dp[i][j]
#             out = 0
#             if s1[i] == s2[j]:
#                 out = helper(i+1, j+1)
#             else:
#                 out = min(ord(s1[i])+helper(i+1, j), ord(s2[j])+helper(i, j+1))
                
#             dp[i][j] = out
#             return out
#         return helper(0, 0)
    
        ## ITERATIVE
        
        
        dp = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
        
        for j in range(len(s2)-1, -1, -1):
            dp[-1][j] = dp[-1][j+1] + ord(s2[j])
            
        for i in range(len(s1)-1, -1, -1):
            dp[i][-1] = dp[i+1][-1] + ord(s1[i])
            
        
        for i in range(len(s1)-1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                    
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i+1][j], ord(s2[j]) + dp[i][j+1])
                    
        return dp[0][0]