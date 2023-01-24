class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        ans = "1"
        
        for i in range(1, n):
            c = 1
            temp = ""
            for j in range(1, len(ans)):
                if ans[j-1] == ans[j]:
                    c+=1
                else:
                    temp += str(c)+ans[j-1]
                    c = 1
            ans = temp + str(c) + ans[-1]
            
            
        return ans
        