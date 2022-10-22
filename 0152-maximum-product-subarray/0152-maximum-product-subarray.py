class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = float("-inf")
        dp = [(0, 0)]*len(nums)
        dp[0] = (nums[0], nums[0])
        ans = max(ans, max(dp[0][0], dp[0][1]))
        for i in range(1, len(nums)):
            
            temp1 = dp[i-1][0]*nums[i]
            temp2 = dp[i-1][1]*nums[i]
            
            a = max(temp2, max(nums[i], temp1))
            b = min(temp1, min(nums[i], temp2))
            
            
            dp[i] = (a,b)
            ans = max(ans, max(dp[i][0], dp[i][1]))

        return ans
                