class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counts = {}
        ans = []
        heap = []
        for i, num in enumerate(nums):
            if num not in counts:
                counts[num] = 0
                
            counts[num] += freq[i]
            
            heapq.heappush(heap, (-counts[num], num))

            while heap and counts[heap[0][1]] != -heap[0][0]:
                heapq.heappop(heap)

            ans.append(-heap[0][0])

        return ans
            