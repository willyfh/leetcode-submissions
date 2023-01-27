class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            neigh_left = float("-inf")
            neigh_right = float("-inf")
            
            if mid>0:
                neigh_left = nums[mid-1]
            if mid < len(nums)-1:
                neigh_right = nums[mid+1]
                
            if  neigh_left < nums[mid] > neigh_right:
                return mid
            elif nums[mid] < neigh_right:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
                
            