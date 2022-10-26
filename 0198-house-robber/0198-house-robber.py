class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        dp[1] = nums[1]
        
        if len(nums) == 3:
            return max(nums[2] + dp[0], dp[1])
        dp[2] = nums[2] + nums[0]
        ans = max(dp[2] ,dp[1])
        
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i])
            ans = max(ans, dp[i])
            
        return ans
        
                