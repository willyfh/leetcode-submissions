class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums)-1
        m = [(nums[j],j)]        
        t = 101 # the largest value is 100
        
        while j>0:
            # find min(nums[x]) such that x > y and a[x] > a[y], then swap
            for k in m:

                if k[0]>nums[j-1]:
                    if  k[0] < t:
                        t = k[0]
                        i_t = k[1]
            
            if t < 101:    
                nums[i_t], nums[j-1] = nums[j-1], nums[i_t]
                break
            else:
                m.append((nums[j-1], j-1))
            j-=1
        
        # sort the remaining array, here I just use a simple sort algorithm with N^2 time complexity
        for i in range(j, len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i]>nums[k]:
                    nums[i], nums[k] = nums[k], nums[i]