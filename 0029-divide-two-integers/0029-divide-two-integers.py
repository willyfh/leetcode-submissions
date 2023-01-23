class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        mi = -2**31
        ma= 2**31 - 1
        neg = False

        if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0):
            neg = True
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        r = divisor
        a = 1
        rem = dividend
        ans = 0
        

            
        while r < dividend:
            while r <= rem:
                prev_a = a
                prev_r = r
                a+=a
                r+=r
                
            if r >= rem:
                ans+= prev_a
                rem = rem - prev_r
                r = divisor
                a = 1
                
            if rem < divisor:
                break
                
                
        if divisor == 1:
            ans=dividend
        if divisor == dividend:
            ans = 1
        if neg:
            ans *=-1
        if ans > ma:
            ans = ma
        if ans < mi:
            ans = mi
        return ans
                
            