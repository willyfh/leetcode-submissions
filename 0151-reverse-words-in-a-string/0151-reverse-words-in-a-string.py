class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        if len(s) == 0:
            return ""
        
        t = s[0]
        for i in range(1, len(s)):
            if s[i]==" " and s[i-1]==" ":
                continue
            t+=s[i]
        arr = t.split(" ")[::-1]        
        return " ".join(arr)
        
        