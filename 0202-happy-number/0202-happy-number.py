class Solution:
    def isHappy(self, n: int) -> bool:
        m =set()
        
        m.add(n)
        
        while True:
            temp = 0
            while n > 0:
                temp+=(n % 10)**2
                n //=10
            if temp == 1:
                return True
            if temp in m:
                return False
            m.add(temp)
            n  = temp