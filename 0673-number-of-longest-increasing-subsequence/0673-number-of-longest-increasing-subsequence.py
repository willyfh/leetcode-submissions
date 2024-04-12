class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        
#         dp = [1]*len(nums)
#         count = [1]*len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     if dp[i] < dp[j] + 1:
#                         dp[i] =  dp[j] + 1
#                         count[i] = count[j]
#                     elif dp[j] + 1 == dp[i]:
#                         count[i]+=count[j]
        

#         m = max(dp)
#         r = 0
#         for i in range(len(dp)):
#             if dp[i] == m:
#                 r += count[i]
#         return r
        
        ### RECURSIVE
    
        memo = {}
        def helper(prev, j):
            
            if j == len(nums):
                return (0, 1)
            
            if (prev,j) in memo:
                return memo[(prev,j)]
            
            
            if nums[j] > prev:
                take, count_take = helper(nums[j], j+1)
                take += 1
                
                dont_take, count_dont_take = helper(prev, j+1)
                
                if take > dont_take:
                    memo[(prev, j)] =(take, count_take)
                elif dont_take > take:
                    memo[(prev, j)] =(dont_take, count_dont_take)
                else:
                    memo[(prev, j)] =(dont_take, count_take+count_dont_take)
                
                
            else:
                dont_take, count_dont_take = helper(prev, j+1)

                memo[(prev, j)] =(dont_take, count_dont_take)
                
            return memo[(prev, j)] 
            
        lis, c = helper(float('-inf'), 0)

        return c