import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        row_map = {}
        col_map = {}
        
        
        rows = ['']*len(grid)
        cols = ['']*len(grid[0])
        
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                rows[j] += "-"+str(grid[j][i])
                cols[i] += "-"+str(grid[j][i])
                
        for r in rows:
            if r not in row_map:
                row_map[r] = 0
            row_map[r] += 1
        
        for c in cols:
            if c not in col_map:
                col_map[c] = 0
            col_map[c] += 1
            
        ans = 0
        for key in row_map:
            if key in col_map:
                ans += (row_map[key]*col_map[key])
        return ans