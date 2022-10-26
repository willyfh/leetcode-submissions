class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        f = set()
        c = [1]
        def helper(i, j, mark):
            if i<0 or j<0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] != "1":
                return
            
            if mark == "1":
                mark = str(c[0]+1)
                c[0] += 1
            grid[i][j] = mark
            f.add(mark)
            
            helper(i+1, j, mark)
            helper(i, j+1, mark)
            helper(i-1, j, mark)
            helper(i, j-1, mark)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                helper(i, j, "1")
                
        return c[0] - 1