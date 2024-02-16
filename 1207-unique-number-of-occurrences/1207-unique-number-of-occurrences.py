class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        unique_occ = set()
        
        for val in arr:
            if val not in hashmap:
                hashmap[val] = 0
            hashmap[val] += 1
        
        for key in hashmap:
            if hashmap[key] not in unique_occ:
                unique_occ.add(hashmap[key])
            else:
                return False
        return True