class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        i=0
        j=(k % (len(nums)))-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
            
        i=k % len(nums)
        j=len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1