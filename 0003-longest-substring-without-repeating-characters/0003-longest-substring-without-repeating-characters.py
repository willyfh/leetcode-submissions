class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        m = {}
        ans = 0
        for i in range(len(s)):
            if s[i] not in m or m[s[i]]<start:  
                ans = max(ans, i-start+1)
            else:
                start = m[s[i]]+1
            m[s[i]] = i                
        return ans