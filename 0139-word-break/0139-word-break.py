class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        wordDict = set(wordDict)
        
        def helper(start):
            
            if start == len(s):
                return True
            
            for end in range(start+1, len(s)+1):
                if dp[start][end] == 1:
                    break
                temp = s[start:end]
                if temp in wordDict:
                    if helper(end):
                        return True
                    dp[start][end] = 1
            return False
        
        return helper(0)
                    