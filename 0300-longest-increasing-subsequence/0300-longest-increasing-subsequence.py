class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        ans = 1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
            ans = max(ans, dp[i])
        return ans
#         @cache
#         def helper(i, prev):
#             if i>=len(nums):
#                 return 0
#             if nums[i] > prev:
#                 l = helper(i+1, prev)
#                 r = 1+helper(i+1, nums[i])
#                 return max(l, r)
#             else:
#                 return helper(i+1, prev)
            
#         return helper(0, -10**5)