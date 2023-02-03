class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        # for index 0 until n-2
        dp1 = [0]*len(nums)     
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        
        
        # for index 1 until n-1 (index 0 is ignored)
        dp2 = [0]*len(nums)
        dp2[0] = 0
        dp2[1] = nums[1]
        
        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])
            dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])
            
        return max(dp1[-2], dp2[-1])