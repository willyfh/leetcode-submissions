class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        dic = {}
        ans = 0
        for i in range(len(s)):
            if s[i] not in dic or dic[s[i]] < start:
                dic[s[i]] = i                
                ans = max(ans, i-start+1)
            else:
                start = dic[s[i]]+1
                dic[s[i]] = i
        return ans