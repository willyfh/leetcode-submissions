class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        d = {}
        ans_key = -1
        ans_value = 0
        for n in nums:
            if n % 2 == 0:
                if n not in d:
                    d[n] = 0
                d[n] += 1
                if ans_value<d[n]:
                    ans_value = d[n]
                    ans_key = n
                elif ans_value == d[n] and n<ans_key:
                    ans_key = n
                    
        return ans_key
                    