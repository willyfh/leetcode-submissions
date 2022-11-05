class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        
        ans = 0
        
        remainder = 0
        for k in d:
            if d[k] % 2 == 0:
                ans+=d[k]
            else:
                if d[k]>1:
                    ans+=d[k]-1
                remainder = 1
                    
            
        return ans + remainder