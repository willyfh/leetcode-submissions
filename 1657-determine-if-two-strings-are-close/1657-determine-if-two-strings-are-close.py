class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        hashmap1 = {}
        hashmap2 = {}
        
        hashmap_val1 = {}
        
        
        for char in word1:
            if char not in hashmap1:
                hashmap1[char] = 0
            hashmap1[char] += 1
            
        for char in word2:
            if char not in hashmap2:
                hashmap2[char] = 0
            hashmap2[char] += 1
            
            if char not in hashmap1:
                return False
            
        for k in hashmap1:
            if k not in hashmap2:
                return False
            if hashmap1[k] not in hashmap_val1:
                hashmap_val1[hashmap1[k]] = 0
            hashmap_val1[hashmap1[k]] += 1
            

        for v in hashmap2.values():
            if v not in hashmap_val1:
                return False
            hashmap_val1[v] -= 1
            if hashmap_val1[v] <0:
                return False
            
        for k in hashmap_val1:
            if hashmap_val1[k] >0:
                return False
        
        return True