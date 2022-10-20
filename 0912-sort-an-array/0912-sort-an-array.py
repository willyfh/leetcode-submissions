class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def mergesort(nums):
            if len(nums)>1 :
                
                mid = len(nums) //2
                
                nl = nums[:mid]
                nr = nums[mid:]
                
                mergesort(nl)
                mergesort(nr)
                
                
                i = 0
                j = 0
                k = 0
                while i<len(nl) and j < len(nr):
                    if nl[i] < nr[j]:
                        nums[k] = nl[i]
                        i+=1
                    else:
                        nums[k] = nr[j]
                        j+=1
                    k+=1
                    
                while i<len(nl):
                    nums[k] = nl[i]
                    i+=1
                    k+=1
                
                while j<len(nr):
                    nums[k] = nr[j]
                    j+=1
                    k+=1
                    
        mergesort(nums)
        return nums