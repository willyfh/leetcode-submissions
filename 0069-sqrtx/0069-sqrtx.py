class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        
        while l<=r:
            m = l+(r-l)//2
            
            if m*m == x:
                return m
            elif m*m>x:
                r = m-1
            else:
                l = m + 1
        return r