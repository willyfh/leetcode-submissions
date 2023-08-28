class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()[::-1]        
        return " ".join(arr)
        
        