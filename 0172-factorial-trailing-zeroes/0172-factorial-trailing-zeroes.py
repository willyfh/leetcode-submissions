class Solution:
    def trailingZeroes(self, n: int) -> int: 
        f= 0
        i = 5
        while i <= n:
            f+=n//i
            i*=5
        return f