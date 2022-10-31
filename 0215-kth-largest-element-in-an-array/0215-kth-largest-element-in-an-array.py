class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for n in nums:
            if len(heap) == k:
                if heap[0]<n:
                    heappop(heap)
                    heappush(heap, n)
            else:
                heappush(heap, n)
        return heap[0]