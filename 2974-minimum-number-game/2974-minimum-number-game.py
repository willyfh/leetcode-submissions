class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        
        sorted_nums = sorted(nums)
        arr = [0 for i in range(len(nums))]
        for i, num in enumerate(sorted_nums):
            
            if i  % 2 == 0:
                arr[i+1] = num
            else:
                arr[i-1] = num
                
        return arr
                