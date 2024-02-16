class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        ans_left = []
        ans_right = []
        
        set_left = set()
        set_right = set()
        
        for num in nums1:
            set_left.add(num)
        for num in nums2:
            set_right.add(num)
            
        
        for num in set_left:
            if num not in nums2:
                ans_left.append(num)
        for num in set_right:
            if num not in nums1:
                ans_right.append(num)
            
        return [ans_left, ans_right]