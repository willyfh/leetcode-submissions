import numpy
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carry = 0
        for i in range(16):
            r = 1 << i
            if a & r and b & r:
                if carry == 1:
                    ans = ans  | r
                else:
                    ans = ans & ~r
                    carry = 1
            elif a & r or b & r:
                if carry == 1:
                    ans = ans & ~r
                else:
                    ans = ans | r
            else:
                if carry == 1:
                    ans = ans | r
                    carry = 0
                else:
                    ans = ans & ~r
        
        return numpy.int16(ans)