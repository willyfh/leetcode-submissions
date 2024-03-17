class Solution:
    def numTilings(self, n: int) -> int:
        self.dp = [0]*(n+1)
        return self.helper(n) % (10**9 + 7)
    
    def helper(self, i):
        if i<1:
            return 1
        if i == 1:
            return 1
        if i==2:
            return 2
        if i==3:
            return 5
        if self.dp[i]>0:
            return self.dp[i]
        self.dp[i] = 2*self.helper(i-1)+self.helper(i-3)
        return self.dp[i]
