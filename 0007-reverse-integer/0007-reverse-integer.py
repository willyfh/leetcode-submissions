class Solution:
    def reverse(self, x: int) -> int:
        
        mi = -2**31
        ma = (2**31)-1
        neg = False
        if x<0:
            neg = True
            x *= -1
        t = x
        ans = 0
        while t != 0: 
            m = t % 10
            ans = 10*ans + m
            if ans > ma or ans < mi: # this assume using long is allowed
                return 0
            t = t // 10
        if neg:
            ans*=-1
        return ans