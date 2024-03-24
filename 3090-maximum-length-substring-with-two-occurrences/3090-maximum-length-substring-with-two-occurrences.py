class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        d = {}
        j =0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 0
            
            d[s[i]] += 1
            if d[s[i]] <3:
                ans = max(ans, i-j+1)
            else:
                while d[s[i]]>= 3:
                    d[s[j]]-=1
                    j+=1
        return ans