class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_arr = s.split(" ")
        
        if len(pattern)!=len(s_arr):
            return False
        
        if len(set(pattern)) != len(set(s_arr)):
            return False
        
        m = {}
        
        for i in range(len(s_arr)):
            
            if s_arr[i] in m and m[s_arr[i]] != pattern[i]:
                
                return False
            m[s_arr[i]] = pattern[i]
            
        return True