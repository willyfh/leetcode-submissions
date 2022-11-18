class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        ## dp solution, n^2 ?
        # dp = [float("inf")] * len(nums)
        # dp[0] = 0
        # for i in range(len(nums)):
        #     for j in range(1, nums[i]+1):
        #         if i+j < len(nums) and dp[i]+1 < dp[i+j]:
        #             dp[i+j] = dp[i]+1
        #             if i+j==len(nums)-1:
        #                 return dp[-1]
        # return dp[-1] # handle [0]
        
        
        left = 0
        right = 0
        
        
        m = 0 # maxreachable
        level = 0
        while right < len(nums)-1:
            m = max(m, left+nums[left])
            
            if left == right:
                right = m
                level += 1
            left += 1
            
        return level