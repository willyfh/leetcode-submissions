class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        ans.append(0)
        for i in range(1, n+1):
            
            temp = 0
            for j in range(32):
                temp+= i&1
                i = i >> 1
            ans.append(temp)
            
        return ans