class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n]+= 1
        
        ans = []
        
        for key in d:
            heappush(ans, (-d[key], key))
        
        return [heappop(ans)[1] for i in range(k)]