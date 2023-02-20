class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums1)):
            if nums1[i] not in hashmap:
                hashmap[nums1[i]] = 0
            hashmap[nums1[i]] += 1
        
        ans = []
        for i in range(len(nums2)):
            if nums2[i] in hashmap and hashmap[nums2[i]] > 0:
                ans.append(nums2[i])
                hashmap[nums2[i]] -= 1
                
        return ans