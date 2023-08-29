class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minLength = len(nums)
        sm = 0
        
        i = 0 
        j = 0
        
        s = nums[0]
        
        if sum(nums) < target:
            return 0
        
        while j < len(nums)-1 or s >= target:
            
            if s < target:
                j+=1
                s+=nums[j]
            else:
                minLength = min(minLength, j-i+1)
                s-=nums[i]
                i+=1
        return minLength