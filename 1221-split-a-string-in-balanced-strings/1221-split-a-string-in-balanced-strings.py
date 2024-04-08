class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        ans = 0
        
        check = 0
        for c in s:
            if c == 'R':
                check+=1
            else:
                check-=1
            if check == 0:
                ans+=1
                
        return ans