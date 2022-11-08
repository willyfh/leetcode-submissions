class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [*nums]
        temp.sort(reverse=True)
        
        j=0
        k = len(nums) //2
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = temp[k]
                k+=1
            else:
                nums[i] = temp[j]
                j+=1