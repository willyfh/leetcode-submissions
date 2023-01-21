class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        state = [[0 for i in range(len(s)+1)] for j in range(len(s))]
        
        ans = s[0]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if i==0:
                    state[j-i][j+1] = 1
                elif i==1:
                    if s[j-i]==s[j]:
                        state[j-i][j+1] = 1
                        ans = s[j-i:j+1]
                else:
                    if s[j-i]==s[j] and state[j-i+1][j]==1:
                        state[j-i][j+1] = 1
                        ans = s[j-i:j+1]
        return ans
                    