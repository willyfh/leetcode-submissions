class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)-1
        n = len(b)-1
        
        
        ans = ""
        
        remainder = False
        while m>=0 and n>=0:
            
            if a[m]=="1" and b[n]=="1":
                if not remainder:
                    ans = "0" + ans
                    remainder = True
                else:
                    ans = "1" + ans
            elif a[m]=="1" or b[n]=="1":
                if not remainder:
                    ans = "1" + ans
                else:
                    ans = "0" + ans
            else:
                if not remainder:
                    ans = "0" +ans
                else:
                    ans = "1" + ans
                    remainder= False
            
            m -=1
            n -=1
        while m>=0:
            if a[m] == "1":
                if not remainder:
                    ans = "1" + ans
                    remainder = False
                else:
                    ans = "0" + ans
            else:
                if remainder:
                    ans = "1" + ans
                    remainder = False
                else:
                    ans = "0" + ans
            m-=1
        while n>=0:
            if b[n] == "1":
                if not remainder:
                    ans = "1" + ans
                    remainder = False
                else:
                    ans = "0" + ans
            else:
                if remainder:
                    ans = "1" + ans
                    remainder = False
                else:
                    ans = "0" + ans
            n-=1
            
        if remainder:
            ans = "1" + ans
        return ans