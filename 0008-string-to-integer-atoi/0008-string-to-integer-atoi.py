class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s)==0:
            return 0
        
        mi = -2**31
        ma = 2**31-1
        
        neg = False
        ans = 0
        i=0
        if s[0] =="-" or s[0]=="+":
            i = 1
            if s[0] == "-":
                neg = True
        
        leading_zero = True
        for x in range(i, len(s)):
            if not s[x].isdigit():
                break
            if s[x] == "0" and leading_zero:
                continue
            elif s[x] != "0":
                leading_zero = False
            ans=ans*10 + int(s[x])
        
                
        if neg:
            ans *= -1
        if ans <mi:
            ans = mi
        if ans > ma:
            ans = ma
        return ans
            
            
            