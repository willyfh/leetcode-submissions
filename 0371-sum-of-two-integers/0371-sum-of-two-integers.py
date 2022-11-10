import numpy
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        neg = False
        if (a <0 and b <0) or (a<0 and -a > b) or (b<0 and -b > a):
            neg = True
        ans = 0
        remainder = 0
        for i in range(32):
            r = 1 << i
            if a & r and b & r:
                if remainder == 1:
                    ans = ans  | r
                else:
                    ans = ans & ~r
                    remainder = 1
            elif a & r or b & r:
                if remainder == 1:
                    ans = ans & ~r
                else:
                    ans = ans | r
            else: # both zeros
                if remainder == 1:
                    ans = ans | r
                    remainder = 0
                else:
                    ans = ans & ~r
        
        return numpy.int32(ans)
                    
             