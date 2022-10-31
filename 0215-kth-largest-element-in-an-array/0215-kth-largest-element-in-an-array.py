class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def helper(left, right):
            
            pivot = right
            temp_left = left
            
            right-=1
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
            
            if left == (len(nums) - k):
                return nums[left]
            elif left < (len(nums) - k):
                return helper(left+1, pivot)
            else: # left > (len(nums) - k)
                return helper(temp_left, left-1)
            
        return helper(0, len(nums)-1)