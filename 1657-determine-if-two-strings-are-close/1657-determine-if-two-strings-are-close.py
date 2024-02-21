class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        
        chars1 = [0]*26
        chars2 = [0]*26
        
        for c in word1:
            chars1[ord(c) - ord('a')] += 1
            
        for c in word2:
            chars2[ord(c) - ord('a')] += 1
            
        for i in range(26):
            if (chars1[i] == 0 and chars2[i]>0) or (chars2[i] == 0 and chars1[i]>0):
                return False
            
        chars1.sort()
        chars2.sort()

        return chars1 == chars2