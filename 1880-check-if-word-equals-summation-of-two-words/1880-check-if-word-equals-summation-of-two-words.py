class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        a = 0
        for f in firstWord:
            a = 10*a + ord(f)-ord('a')
            
        b = 0
        for s in secondWord:
            b = 10*b + ord(s)-ord('a')
            
        c = 0
        for t in targetWord:
            c = 10*c + ord(t)-ord('a')
            
        return a+b == c