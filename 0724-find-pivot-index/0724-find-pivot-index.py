class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        s = sum(nums)
        t = 0
        for i in range(len(nums)):
            s-=nums[i]
            if t == s:
                return i
            t+=nums[i]
            
        return -1