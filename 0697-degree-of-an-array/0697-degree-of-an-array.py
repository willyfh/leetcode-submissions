class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        d_init = {}
        d_end = {}
        
        ma = 0
        num_ma = []
        for i in range(len(nums)):
            num = nums[i]
            if num not in d:
                d[num] = 0
            d[num] += 1
            
            if d[num] > ma:
                num_ma = [num]
                ma = d[num]
            elif d[num] == ma:
                num_ma.append(num)
                
            if num not in d_init:
                    d_init[num] = i
                    d_end[num] = i
            if i > d_end[num]:
                d_end[num] = i
                
        ans = 50000 # max length in the constraint
        
        for num in num_ma:
            ans = min(ans, d_end[num] - d_init[num] + 1)
            
        return ans
        
            
        