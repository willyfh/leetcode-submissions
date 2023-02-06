class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mi = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > mi:
                ans = max(prices[i] - mi, ans)
            else:
                mi = prices[i]
                
        return ans