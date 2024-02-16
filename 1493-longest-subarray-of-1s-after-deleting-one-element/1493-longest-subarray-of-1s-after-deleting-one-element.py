class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        left = 0
        num_zeros = 0
        tot_zeros = 0
        ans = 0
        
        for right in range(len(nums)):            
            if nums[right] == 0:
                num_zeros += 1
                tot_zeros += 1
                if num_zeros==1:
                    continue
            if num_zeros >1:
                if nums[left] ==0:
                    num_zeros-=1
                left+=1
                
                
            if num_zeros ==1 :
                ans = max(ans, right-left)
            elif num_zeros ==0:
                ans = max(ans, right-left+1)
        if tot_zeros == 0:
            return ans-1
        return ans
                
    