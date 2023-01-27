class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = nums[0]
        
        i=0
        j=len(nums)-1
        
        fromleft = 1
        fromright = 1
        while i <len(nums):
            fromleft *= nums[i]
            fromright *= nums[j]
            ans = max(ans, fromleft)
            ans = max(ans, fromright)
            
            if fromleft == 0:
                fromleft=1
            if fromright==0:
                fromright=1
            i+=1
            j-=1
        return ans
            