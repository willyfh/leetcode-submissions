class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        

        h = []
        
        pairs = list(zip(nums1, nums2))

        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)


        h = [sorted_pairs[i][0] for i in range(k)]
        heapify(h)
        
        s = sum(h)
        ans = sorted_pairs[k-1][1] * s
        for i in range(k, len(sorted_pairs)):
            s+=sorted_pairs[i][0]
            r = heappushpop(h, sorted_pairs[i][0])
            s-= r
            ans = max(ans, sorted_pairs[i][1]*s)
            
        
        return ans