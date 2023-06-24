class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                i+=1
            else:
                nums[i], nums[k] = nums[k], nums[i]
                k+=1
                i+=1
                
        return k
        