class Solution:
    def romanToInt(self, s: str) -> int:
        
        m = {}
        m['I'] = 1
        m['V'] = 5
        m['X'] = 10
        m['L'] = 50
        m['C'] = 100
        m['D'] = 500
        m['M'] = 1000
        
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        
        ans = 0
        for i in range(len(s)):
            ans+= m[s[i]]
            
        return ans