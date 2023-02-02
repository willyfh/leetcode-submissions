class Solution:
    def rob(self, nums: List[int]) -> int:
        dp  = [0] * len(nums)
        
        a = nums[0]
        if len(nums)==1:
            return a
        b = max(nums[1], nums[0])
        c = b
        for i in range(2, len(nums)):
            c = max(nums[i]+a, b)
            a = b
            b = c
        return c