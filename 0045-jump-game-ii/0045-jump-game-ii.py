class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                if i+j < len(nums) and dp[i]+1 < dp[i+j]:
                    dp[i+j] = dp[i]+1
        return dp[-1]