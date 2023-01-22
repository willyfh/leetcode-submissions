class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        j=0
        i=0
        
        if len(needle)>len(haystack):
            return -1
        
        for i in range(len(haystack)):
            while j  < len(needle):
                if i+j < len(haystack) and needle[j] == haystack[i+j]:
                    j+=1
                else:
                    break
                if j==len(needle):
                    return i
            j=0
        return -1