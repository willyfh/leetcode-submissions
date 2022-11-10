import numpy
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        i =0
        for i in range(16):
            c = a & b # carry. 1+1 have carry
            a = a ^ b # "addition". eg. 1+0= 1, 1+1=0, 0+0=0
            b = c << 1 # shifting carry to the left
        
        return numpy.int16(a)