class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev = (nums[0], nums[0])
        ans = prev[0]
        for i in range(1, len(nums)):
            
            candidates = [nums[i], prev[0]*nums[i], prev[1]*nums[i]]
                        
            current = (max(candidates), min(candidates))
            ans = max(ans, current[0])
            prev = current

        return ans
                