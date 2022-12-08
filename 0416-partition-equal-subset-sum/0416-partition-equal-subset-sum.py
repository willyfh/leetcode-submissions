class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 !=0: #odd
            return False
        
        half = total / 2
        
        
        dp  = [0 for j in range(total)]
        @cache
        def helper(left, right, k):
            if left == right and left!=0 and k==len(nums):
                return True
            if left > half or right > half:
                return False
            if k>=len(nums):
                return False
            a = helper(left+nums[k], right, k+1)
            b = helper(left, right+nums[k], k+1)
            return a or b
                
        return helper(0,0, 0)
            