class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [[-1]*len(t) for i in range(len(s))]
        
        
        def helper(seq, i, j):
            if seq == t:
                return 1
            if i == len(s):
                return 0
            if dp[i][j] > -1:
                return dp[i][j]
            out = 0
            if s[i] == t[j]:
                
                out = helper(seq+s[i], i+1, j+1)
                
                out+= helper(seq, i+1, j)
                
            else:
                out = helper(seq, i+1, j)
            
            dp[i][j] = out
            return out
            
        return helper("", 0, 0)