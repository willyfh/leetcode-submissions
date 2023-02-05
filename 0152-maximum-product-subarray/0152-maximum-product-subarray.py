class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        mi = nums[0]
        ma = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            candidates = [nums[i], ma*nums[i], mi*nums[i]]
            ma = max(candidates)
            mi = min(candidates)
            ans = max(ans, ma)
            
        return ans
        