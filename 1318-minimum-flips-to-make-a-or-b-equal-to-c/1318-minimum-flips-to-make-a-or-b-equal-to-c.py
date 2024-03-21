class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        ans = 0
        for i in range(31):
            check_a = a & 1
            check_b = b & 1
            check_c = c & 1
            
            if check_c ==1:
                if check_a == 0 and check_b == 0:
                    ans+=1
            else:
                ans += check_a + check_b
            
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return ans