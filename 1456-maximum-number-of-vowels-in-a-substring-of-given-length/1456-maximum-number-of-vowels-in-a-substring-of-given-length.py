class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vow = {'a', 'i', 'u', 'e', 'o'}
        v = 0
        for i in range(k):
            if s[i] in vow:
                v+=1
        ans = v
        for i in range(len(s)-k):
            
            if s[i] in vow:
                v-=1
            if s[i+k] in vow:
                v+=1
            
            ans = max(ans, v)
        return ans