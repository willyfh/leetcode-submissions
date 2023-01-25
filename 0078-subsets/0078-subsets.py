class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        def helper(s, i):
            subsets.append(s)
            
            for j in range(i, len(nums)):
                helper(s+[nums[j]], j+1)
                
        helper([], 0)
        return subsets