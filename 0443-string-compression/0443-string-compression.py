class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        s =  chars[0]
        n = 1
        t = 1
        for i in range(1, len(chars)):
            if chars[i] == s:
                n+=1
            else:
                chars[t-1] = s

                s = chars[i]
                if n > 1:
                    st = str(n)
                    for a in st:
                        chars[t] = a
                        t+=1
                    t+=1
                else:
                    t+=1
                n=1
                    
        chars[t-1] = s   
        if n>1:
            
            st = str(n)
            for a in st:
                chars[t] = a
                t+=1
        chars[:t]
        return t