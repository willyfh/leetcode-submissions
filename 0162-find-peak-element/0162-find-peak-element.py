class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        left = float("-inf")
        right = nums[1]
        for i in range(len(nums)):
            if left < nums[i] > right:
                return i
            left = nums[i]
            if i == len(nums)-2:
                right = float("-inf")
            else:
                right = nums[i+2]
        return -1