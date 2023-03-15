class Solution:
    def countOdds(self, low: int, high: int) -> int:
        r = high - low + 1 # the number of digit inclusive
        
        if r % 2 == 0:
            return r // 2
        else:
            if low % 2 == 1:
                return r//2 + 1
            else:
                return r//2
        