class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 0
            hashmap[s[i]] += 1
            
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1
                