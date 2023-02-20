class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        i = 0
        while i<32:
            ans = ans << 1
            ans = ans | n & 1
            n = n >> 1
            i+=1
            
        return ans