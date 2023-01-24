class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + temp > 0 and nums[i]<nums[i]+temp:
                temp += nums[i]
            else:
                temp = nums[i]
            ans = max(ans, temp)
        return ans