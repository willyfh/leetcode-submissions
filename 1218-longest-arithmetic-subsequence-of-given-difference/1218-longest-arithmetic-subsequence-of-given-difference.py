class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        k = difference
        dp = {}
        ans = 1
        for i in range(len(arr)):
            
            if arr[i] - k in dp:
                dp[arr[i]] = dp[arr[i]-k] + 1
            else:                    
                dp[arr[i]] =1
            ans = max(ans, dp[arr[i]])
        return ans