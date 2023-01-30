class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        zero = False
        for i in range(len(nums)):
            s += nums[i]
            if nums[i] == 0:
                zero = True
        
        n = len(nums)
        
        t = n * (n+1) // 2
        
        ans = t - s
        if ans ==0 and zero:
            return n
        return t - s