class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        n = numerator
        d = denominator
        ans = []
        m = {}
        i = 0
        
        n = abs(n)
        d = abs(d)
        neg = False
        if  (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            neg = True
        if n==0:
            return "0"
        while n!=0:
            if n // d == 0:
                n*=10
                ans.append("0")
            else:
                r = n // d
                ans.append(str(r))
                n -= (r * d)
                n*=10
            if n in m:
                ans = ans[0:1]+["."]+ans[1:m[n]+1] + ["("] + ans[m[n]+1:i+1] +[")"]
                if neg:
                    ans.insert(0,"-")
                return "".join(ans)
            m[n] = i
            i += 1
        if numerator % denominator !=0:
            ans = ans[0:1]+["."]+ans[1:]
        if neg:
            ans.insert(0,"-")
        return "".join(ans)