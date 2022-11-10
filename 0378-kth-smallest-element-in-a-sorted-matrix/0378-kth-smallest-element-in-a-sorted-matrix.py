class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        
        h = []
        for i in range(n):
            for j in range(n):
                heappush(h, -matrix[i][j])
                if len(h)>k:
                    heappop(h)
                    
        return -heappop(h)