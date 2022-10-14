class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        def helper(i, s, c, dp):
            if i==0:
                if c[0]!="0" and int(c)>=1 and int(c) <=26:
                    return 1
                else:
                    return 0
            
            if i==len(s) or (c[0]!="0" and int(c) >=1 and int(c) <=26):
                if dp[i]!=-1:
                    return dp[i]
                a = helper(i-1, s, s[i-1], dp)
                if i-2>=0:
                    a += helper(i-2, s, s[i-2:i], dp)
            else:
                a = 0
            
            dp[i] = a
            return a
            
        dp = [-1]*(len(s)+1)
        return helper(len(s), s, "", dp)