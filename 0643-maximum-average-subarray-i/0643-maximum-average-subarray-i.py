class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        s = 0
        ans = float("-inf")
        
        i=0
        j=0
        
        while j < len(nums):
            
            s+=nums[j]
            j+=1           
            
            if j-i == k:
                ans = max(ans, s/k)
                s-=nums[i]
                i+=1
        return ans