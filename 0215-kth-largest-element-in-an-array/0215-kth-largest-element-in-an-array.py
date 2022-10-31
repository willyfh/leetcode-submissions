class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
            
        def partition(left, right):
            pivot = right
            right -= 1
            while left<=right:
                while nums[left] < nums[pivot]:
                    left += 1
                while nums[right] > nums[pivot]:
                    right -= 1
                
                if left>=right:  
                    break

                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
                
            nums[left], nums[pivot] = nums[pivot], nums[left]
            return left
        
        left = 0
        right = len(nums) -1
        
        while left < right:
            p = partition(left, right)
            if p == (len(nums) - k):
                return nums[p]
            elif p < (len(nums) - k):
                left = p + 1
            else: # p > (len(nums) - k)
                right = p -1
        return nums[left]
