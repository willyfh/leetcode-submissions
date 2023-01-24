class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        perm_list = []
        
        def helper(perm, visited):
            if len(perm)==len(nums):
                perm_list.append([*perm])
                return
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    helper(perm+[nums[i]],visited)
                    visited.remove(nums[i])
            
        helper([], set())
        return perm_list