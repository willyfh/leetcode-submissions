class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = None
        second = nums[0]
        for i in range(1, len(nums)):
            
            if nums[i]>second:
                if first!=None:
                    return True
                first = second
                second=nums[i]
            elif nums[i] < second:
                    if first==None or nums[i] > first:
                        second = nums[i]
                    else:
                        first = nums[i]
        return False