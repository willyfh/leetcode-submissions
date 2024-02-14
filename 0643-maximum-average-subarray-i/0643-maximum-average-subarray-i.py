class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        s = 0
        
        s = sum(nums[:k])
        ans = s/k
        
        for i in range(len(nums)-k):
            
            s -= nums[i]
            s += nums[i+k]
            
            ans = max(ans, s / k)
            
        return ans