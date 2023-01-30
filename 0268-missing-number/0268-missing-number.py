class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            s += nums[i]
        
        n = len(nums)
        
        t = n * (n+1) // 2
        
        ans = t - s

        return t - s