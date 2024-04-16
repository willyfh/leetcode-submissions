class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        dp = [{} for i in range(len(nums))]
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] - nums[j] in dp[j]:
                     dp[i][nums[i] - nums[j]] = dp[j][nums[i] - nums[j]] + 1
                else:
                    dp[i][nums[i] - nums[j]] = 2
                ans = max(ans, dp[i][nums[i] - nums[j]])
      
                
        return ans
        