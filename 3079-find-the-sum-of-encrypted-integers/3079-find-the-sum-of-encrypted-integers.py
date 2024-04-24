class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        ans = 0
        
        for num in nums:
            str_num = str(num)
            m = 0
            for s in str_num:
                
                m = max(m, int(s))
            t = m
            for i in range(1, len(str_num)):
                t = t*10 + m
            ans += t
            
        return ans
                