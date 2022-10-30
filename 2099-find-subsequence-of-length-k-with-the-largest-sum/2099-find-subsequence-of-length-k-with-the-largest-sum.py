import numpy
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        idx   = numpy.argsort(nums)

        return [nums[i] for i in sorted(idx[-k:])]
