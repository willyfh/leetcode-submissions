class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        
        dp = [1]*len(nums)
        count = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] =  dp[j] + 1
                        count[i] = 0
                    if dp[j] + 1 == dp[i]:
                        count[i]+=count[j]
        

        m = max(dp)
        r = 0
        for i in range(len(dp)):
            if dp[i] == m:
                r += count[i]
        return r
        