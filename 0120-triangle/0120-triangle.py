class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        
        @cache
        def helper(i, j):
            if i==n-1:
                return triangle[i][j]
                
            return triangle[i][j] + min(helper(i+1, j), helper(i+1, j+1))
            
        return helper(0, 0)