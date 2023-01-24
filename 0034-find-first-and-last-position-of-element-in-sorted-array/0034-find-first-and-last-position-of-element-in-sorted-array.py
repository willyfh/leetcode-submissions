class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) -1
        start = -1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                if (mid==0 or nums[mid-1] != target):
                    start = mid
                    break 
                else:
                    right = mid-1
            elif nums[mid] < target:
                left = mid + 1
            else: # nums[mid] > target
                right = mid - 1
        left = 0
        right = len(nums) -1
        end = -1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                if (mid==len(nums)-1 or nums[mid+1] != target):
                    end = mid
                    break
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            
            else: # nums[mid] > target
                right = mid - 1
        return [start, end]