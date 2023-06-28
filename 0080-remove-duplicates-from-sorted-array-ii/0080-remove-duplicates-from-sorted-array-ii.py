class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_val = nums[0] # last valid value
        last_index = 0 # last valid index (no duplicaate more  than 2)
        c = 0 # for checking duplicate
        k=1 # final k element
        for i in range(1, len(nums)):
            if nums[i] != last_val:
                last_val = nums[i]
                nums[last_index+1] = nums[i]
                last_index = last_index+1
                c=0
                k+=1
            else:
                if c==0:
                    nums[last_index+1] = nums[i]
                    last_index += 1
                    c+=1
                    k+=1
        return k