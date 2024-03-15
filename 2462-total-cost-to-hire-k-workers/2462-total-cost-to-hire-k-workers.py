class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
       
        
        
        left = candidates - 1
        right = len(costs)- candidates
        
        overlap = 0
        if left>=right:
            
            overlap = left-right+1
            
        right += overlap
        
        heap_left = costs[:left+1]
        
        heap_right = costs[right:]
        heapify(heap_left)
        heapify(heap_right)
        
        total = 0
        
        for i in range(k):
            
            if heap_left and heap_right and heap_left[0] <= heap_right[0]:
                left+=1
                c = heappop(heap_left)
                if left<right:
                    heappush(heap_left, costs[left])
            else:
                if heap_right:
                    right-=1
                    c = heappop(heap_right)
                    if left<right:
                        heappush(heap_right, costs[right])
                else:
                    left+=1
                    c = heappop(heap_left)
            total += c
            
            
        return total