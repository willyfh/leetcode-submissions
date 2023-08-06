class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = {}
        
        for n in nums:
            if n not in c:
                c[n] = 0
            c[n] += 1
            
        for k in c:
            if c[k] > len(nums)/2:
                return k
            
        return -1