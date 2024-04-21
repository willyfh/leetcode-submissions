class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        ans = 0
        prev = s[0].lower()
        for i in range(1, len(s)):
            if s[i].lower() != prev:
                ans+=1
                
            prev = s[i].lower()
            
        return ans
            