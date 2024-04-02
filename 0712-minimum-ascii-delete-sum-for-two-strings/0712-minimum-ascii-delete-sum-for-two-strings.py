class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        dp = [[0]*len(s2) for i in range(len(s1))]
        
        def helper(i, j):
            if i == len(s1):
                s = 0
                for k in s2[j:]:
                    s+=ord(k)
                return s
            elif j==len(s2):
                s = 0
                for k in s1[i:]:
                    s+=ord(k)
                return s
            if dp[i][j] >0:
                return dp[i][j]
            out = 0
            if s1[i] == s2[j]:
                out = helper(i+1, j+1)
            else:
                out = min(ord(s1[i])+helper(i+1, j), ord(s2[j])+helper(i, j+1))
                
            dp[i][j] = out
            return out
        return helper(0, 0)