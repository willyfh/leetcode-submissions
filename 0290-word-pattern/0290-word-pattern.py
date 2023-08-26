class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_arr = s.split(" ")
        
        if len(pattern)!=len(s_arr):
            return False
        
        m = {}
        n = {}
        
        for i in range(len(pattern)):
            
            if pattern[i] in m and m[pattern[i]] != s_arr[i] or pattern[i] not in m and s_arr[i] in n:
                
                return False
            m[pattern[i]] = s_arr[i]
            n[s_arr[i]] =  1
            
        return True