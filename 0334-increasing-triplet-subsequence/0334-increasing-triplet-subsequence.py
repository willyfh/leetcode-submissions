class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        temp = [nums[0]] # to store tripplet
        
        for i in range(1, len(nums)):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
                if len(temp)==3:
                    return True
            elif nums[i] < temp[-1]:
                    if nums[i] > temp[0]:
                        temp[-1] = nums[i]
                    else:
                        temp[0] = nums[i]
        return False