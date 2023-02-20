class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(prefix)):
                if j == len(strs[i]):
                    prefix = prefix[:j]
                    break
                if strs[i][j]!=prefix[j]:
                    prefix = prefix[:j]
                    break                    
        return prefix