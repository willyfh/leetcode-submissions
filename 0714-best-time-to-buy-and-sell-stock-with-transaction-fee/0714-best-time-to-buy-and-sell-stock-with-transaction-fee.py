class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        self.prices = prices
        return self.helper(0, True, fee)
    
    @cache
    def helper(self, i, buy, fee):
        
        if i == len(self.prices):
            if buy:
                return 0
            else:
                return float('-inf')
        
        if buy:
            ans =  max(self.helper(i+1, False, fee) - self.prices[i], self.helper(i+1, True, fee))
        else:
            ans = max(self.helper(i+1, True, fee) + self.prices[i] - fee, self.helper(i+1, False, fee))
        return ans
        