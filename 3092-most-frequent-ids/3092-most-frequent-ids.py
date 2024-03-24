class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        d = {}
        ans = []
        max_heap = []
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = 0
                
            d[num] += freq[i]
            
            heapq.heappush(max_heap, (-d[num], num))

            while max_heap and d[max_heap[0][1]] != -max_heap[0][0]:
                heapq.heappop(max_heap)

            ans.append(-max_heap[0][0])

        return ans
            