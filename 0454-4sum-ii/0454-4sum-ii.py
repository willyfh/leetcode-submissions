class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        d1 = {}
        for x in nums1:
            if x not in d1:
                d1[x] = 0
            d1[x] += 1
        
        d2 = {}
        for x in nums2:
            if x not in d2:
                d2[x] = 0
            d2[x] += 1
            
        d3 = {}
        for x in nums3:
            if x not in d3:
                d3[x] = 0
            d3[x] += 1
            
        d4 = {}
        for x in nums4:
            if x not in d4:
                d4[x] = 0
            d4[x] += 1
        
        ans = 0
        
        d5 = {}
        for m in d1.keys():
            for n in d2.keys():
                if m+n not in d5:
                    d5[m+n] = 0
                d5[m+n] += d1[m]*d2[n]
        
        for m in d5.keys():
            for o in d3.keys():
                if -(m+o) in d4:
                    ans += d5[m]* d3[o]*d4[-(m+o)]
        return ans