class Solution:
    def pivotInteger(self, n: int) -> int:
        t = 0
        for i in range(1, n+1):
            t += i
        
        s = 0
        for i in range(1, n+1):
            s += i
            
            if s == t-s+i:
                return i
            
        return -1