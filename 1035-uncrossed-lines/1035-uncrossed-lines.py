class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        dp = [[-1]*len(nums2) for _ in range(len(nums1))]
        
        def helper(i, j):
            if i==len(nums1) or j == len(nums2):
                return 0
            if dp[i][j] > -1:
                return dp[i][j]
            
            if nums1[i] == nums2[j]:
                dp[i][j] = 1+helper(i+1, j+1)
                
            else:
                dp[i][j] = max(helper(i+1, j), helper(i, j+1))
            
            return dp[i][j]
        
        return helper(0, 0)