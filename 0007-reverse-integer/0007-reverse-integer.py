class Solution:
    def reverse(self, x: int) -> int:
        
        mi = -2**31
        ma = (2**31)-1
        
        neg = False
        if x < 0:
            neg = True
            x *= -1
            
        t = x
        ans = 0
        while t > 0: 
            m = t % 10
            ans = 10*ans + m
            t = t // 10
        if neg:
            ans *= -1
        if ans < mi or ans > ma:
            ans = 0
        return ans