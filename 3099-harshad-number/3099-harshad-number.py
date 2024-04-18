class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        d = 0
        init_x = x
        while x>0:
            d+= x%10
            x = x//10
            
        return int(d) if init_x%d==0 else -1