class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 0
            m[s[i]] += 1
            
        for i in range(len(t)):
            if t[i] in m and m[t[i]] > 0:
                m[t[i]] -= 1
            else:
                return False
            
        for k in m:
            if m[k] >0 :
                return False
        return True