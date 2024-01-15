class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        
        m = len(str1)
        n = len(str2)
        
        l = min(m, n)
        
        while l >0:
            
            if m%l==0 and n%l==0:
                
                s1 = int(m/l)
                s2 = int(n/l)
                
                pat = str1[:l]
                eq = True
                for i in range(1, s1):
                    if pat!=str1[l*i:l*i+l]:
                        eq = False
                        break
                        
                for i in range(0, s2):
                    if pat!=str2[l*i:l*i+l]:
                        eq = False
                        break
                if eq:
                    return pat
            l-=1
                
        return ""