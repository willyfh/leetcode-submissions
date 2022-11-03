class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        i=1
        j=len(nums)-2
        
        ans = [1]*len(nums)
        pre  = 1
        suf = 1
        while i<len(nums):
            pre *= nums[i-1]
            ans[i] = ans[i]*pre
            suf *= nums[j+1]
            ans[j] = ans[j]*suf
            i+=1
            j-=1
        
        
        return ans
            
        
        