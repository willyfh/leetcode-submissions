class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        d = deque()
        
        for i in range(0, len(asteroids)):

            if len(d)==0 or not(asteroids[i] < 0 and d[-1] > 0):
                d.append(asteroids[i])
            else:
    
                while len(d)>0 and d[-1] > 0 and d[-1] < abs(asteroids[i]):
                    d.pop()
            
                if len(d) == 0 or d[-1]<0:
                    d.append(asteroids[i])
                else:
                    if d[-1] == abs(asteroids[i]):
                        d.pop()

                
        return d
                