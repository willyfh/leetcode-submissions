class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        
        t = 0
        for i in range(0, len(nums)+1):
            t+=i
            
        return t - s