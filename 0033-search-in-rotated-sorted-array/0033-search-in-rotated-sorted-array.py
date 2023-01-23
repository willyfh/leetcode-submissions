class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if target>=nums[left] or nums[mid]<nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if target <=nums[right] or nums[mid]>nums[right]:
                    left = mid+1
                else:
                    right = mid -1
                
            
        return -1