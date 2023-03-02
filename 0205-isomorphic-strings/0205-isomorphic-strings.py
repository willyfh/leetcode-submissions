class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        
        m = {}
        n = {}
        
        for i in range(len(t)):
            if t[i] not in n and s[i] not in m:
                n[t[i]] = s[i]
                m[s[i]] = t[i]
            elif t[i] not in n:
                return False
            elif s[i] not in m:
                return False
            else:
                if not(n[t[i]] == s[i] and m[s[i]] == t[i]):
                    return False
                
        return True