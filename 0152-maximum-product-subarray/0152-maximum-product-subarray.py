class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dp = [[0, 0]]*len(nums)
        dp[0] = (nums[0], nums[0])
        ans = dp[0][0]
        for i in range(1, len(nums)):
            
            candidates = [nums[i], dp[i-1][0]*nums[i], dp[i-1][1]*nums[i]]
                        
            dp[i][0] = max(candidates)
            dp[i][1] = min(candidates)
            ans = max(ans, dp[i][0])

        return ans
                