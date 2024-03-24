class Solution:
    def minOperations(self, k: int) -> int:
        
        self.sum = 1
        
        @cache
        def helper(val):
            if self.sum>=k:
                return 0
                
            self.sum+= 1
            inc = 1 + helper(val+1)
            self.sum -=1
            
            self.sum += val
            dup = 1 + helper(val)
            self.sum -=val
            
            return min(inc, dup)
        
        return helper(1)