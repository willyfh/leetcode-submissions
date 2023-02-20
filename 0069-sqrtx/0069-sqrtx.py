class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        
        while l<=r:
            m = l+(r-l)//2
            
            if m*m <= x < (m+1)*(m+1):
                return m
            elif m*m>x:
                r = m
            else:
                l = m
        return x