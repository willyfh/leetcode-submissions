class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for i in range(len(nums)):
            n = nums[i]
            if -(n-target) in hashmap:
                return [hashmap[-(n-target)], i]
            hashmap[n] = i