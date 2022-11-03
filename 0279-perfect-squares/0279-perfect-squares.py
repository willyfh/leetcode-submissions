import numpy
class Solution:

    def numSquares(self, n: int) -> int:
        
        q = deque()
        
        q.append((n,1));
            
        while len(q)>0:
            
            curr, lvl = q.popleft()
            
            s = int(numpy.sqrt(curr))
            
            i = s
            while i>0:
                a = curr - (i**2)
                if a>0:
                    q.append((a, lvl+1))
                elif a == 0:
                    return lvl
                i-=1
        return -1
            
            