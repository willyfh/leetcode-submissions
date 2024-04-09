class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = set()
        d2 = set()
        
        for num1 in nums1:
            d1.add(num1)
            
        for num2 in nums2:
            d2.add(num2)
            
        f, s = 0, 0
        
        for num1 in nums1:
            if num1 in d2:
                f+=1
        for num2 in nums2:
            if num2 in d1:
                s+=1
        return [f, s]