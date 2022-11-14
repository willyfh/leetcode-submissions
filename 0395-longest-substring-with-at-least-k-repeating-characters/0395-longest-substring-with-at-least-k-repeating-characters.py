class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        ans = 0
        
        c = {}
        for a in s:
            if a not in c:
                c[a] = 0
            c[a] += 1
        
        
        for i in range(len(s)):
            m = {} # more than or equal to k
            l = {} # less than k
            for j in range(i, len(s)):
                if c[s[j]]<k:
                    break
                if s[j] not in m:
                    if s[j] not in l:
                        l[s[j]] = k
                    l[s[j]]-=1
                    if l[s[j]] == 0:
                        del l[s[j]]
                        if len(l) == 0:
                            ans = max(ans, j-i+1)
                        m[s[j]] = 1
                else:
                    if len(l) == 0:
                        ans = max(ans, j-i+1)
        return ans