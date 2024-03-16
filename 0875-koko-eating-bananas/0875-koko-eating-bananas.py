class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (left+right) // 2
            t = self.count(piles, mid)
            
            if t>h:
                left = mid + 1
            else:
                right = mid - 1
        return left
                
    
    def count(self, piles, k):
        t = 0
        for p in piles:
             t += math.ceil(p/k)
                
        return t