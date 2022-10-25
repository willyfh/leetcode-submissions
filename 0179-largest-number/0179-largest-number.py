class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        
        def mergesort(arr):
            if len(arr)==1:
                return
            
            mid = len(arr)//2
            
            left = arr[:mid]
            right = arr[mid:]
            
            mergesort(left)
            mergesort(right)
            
            merge(left, right, arr)
            
        def merge(left, right, arr):
            i=0
            j=0
            k=0
            while i < len(left) and j<len(right):
                
                l  = int(str(left[i])+str(right[j]))
                r = int(str(right[j])+str(left[i]))
                if l > r:
                    arr[k] = left[i]
                    k+=1
                    i+=1
                else:
                    arr[k] = right[j]
                    k+=1
                    j+=1
            while i<len(left):
                arr[k] = left[i]
                i+=1
                k+=1
                
            while j<len(right):
                arr[k] = right[j]
                k+=1
                j+=1
        mergesort(nums)
        if sum(nums)==0:
            return "0"
        return "".join([str(n) for n in nums])