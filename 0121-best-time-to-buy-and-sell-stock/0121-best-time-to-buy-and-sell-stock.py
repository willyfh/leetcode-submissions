class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mi = prices[0]
        
        for i in range(1, len(prices)):
            mi = min(mi, prices[i])
            
            ans = max(ans, prices[i] - mi)
            
        return ans