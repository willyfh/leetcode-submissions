class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        d = deque()
        d.append(asteroids[0])
        
        for i in range(1, len(asteroids)):
            if len(d)==0:
                d.append(asteroids[i])
                continue
            if not(asteroids[i] < 0 and d[-1] > 0):
                d.append(asteroids[i])
            else:
    
                while len(d)>0 and d[-1] > 0 and d[-1] < abs(asteroids[i]):
                    d.pop()
            
                if len(d)>0:
                    if d[-1] == abs(asteroids[i]):
                        d.pop()
                    elif d[-1]<0:
                        d.append(asteroids[i])
                else:
                    d.append(asteroids[i])

                
        return d
                