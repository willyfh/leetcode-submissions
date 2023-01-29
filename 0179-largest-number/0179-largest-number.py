class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def merge(left, right):
            i = 0
            j = 0
            result = []
            while i < len(left) and j < len(right):
                if str(left[i])+str(right[j]) > str(right[j])+str(left[i]):
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            
            while i<len(left):
                result.append(left[i])
                i+=1
            while j<len(right):
                result.append(right[j])
                j+=1
            return result
        
        def mergesort(arr):
            if len(arr)<=1:
                return arr
            
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            
            left = mergesort(left)
            right = mergesort(right)
            return merge(left, right)
        
        sorted_arr = mergesort(nums)
        if sorted_arr[0] == 0:
            return "0"
        ans = ""
        for i in range(len(sorted_arr)):
            ans += str(sorted_arr[i])
        return ans

        