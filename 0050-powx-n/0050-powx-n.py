class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        ans = 1
        
        neg = False
        if n<0:
            neg = True
            n = abs(n)
        r = x
        a =1
        while a <= n:
            while a+a <= n:
                
                a+=a
                r*=r
            ans *= r
            n-=a
            a=1
            r = x
        if neg:
            return 1/ans
        return ans
            