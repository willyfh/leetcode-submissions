class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        hashmap1 = {}
        hashmap2 = {}
        
        
        for char in word1:
            if char not in hashmap1:
                hashmap1[char] = 0
            hashmap1[char] += 1
            
        for char in word2:
            if char not in hashmap2:
                hashmap2[char] = 0
            hashmap2[char] += 1
            
        for k in hashmap1:
            if k not in hashmap2:
                return False
            
        for k in hashmap2:
            if k not in hashmap1:
                return False
            
        values1 = list(hashmap1.values())
        values2 = list(hashmap2.values())
        values1.sort()
        values2.sort()
        
        if len(values1) != len(values2):
            return False
        
        for i in range(len(values1)):
            if values1[i] != values2[i]:
                return False        
        
        return True