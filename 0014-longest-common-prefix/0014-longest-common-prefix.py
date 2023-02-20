class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]
        for i in range(1, len(strs)):
            cont = False
            for j in range(len(strs[i])):
                if j>=len(prefix):
                    break
                if prefix[j] == strs[i][j]:
                    cont =True
                    continue
                else:
                    prefix = prefix[:j]
                    break
            if cont:
                prefix = prefix[:j+1]
            if len(strs[i])==0:
                prefix = ""
            
                    
        return prefix