class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        sets1 = set(nums1)
        sets2 = set(nums2)
        a1 = []
        a2 = []
        for n1 in sets1:
            if n1 not in sets2:
                a1.append(n1)
        for n2 in sets2:
            if n2 not in sets1:
                a2.append(n2)
        return [a1, a2]