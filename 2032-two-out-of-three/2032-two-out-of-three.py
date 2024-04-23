class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        s = set()
        ans = set()
        
        for x in nums1:
            s.add(x)
        
        t = set()
        for x in nums2:
            if x in s:
                ans.add(x)
            t.add(x)
        s.update(t)
        for x in nums3:
            if x in s:
                ans.add(x)
            
        return ans