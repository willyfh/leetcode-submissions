class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        row_map = {}
        
        for i in range(len(grid)):
            t = tuple(grid[i])
            if t not in row_map:
                row_map[t] = 0
            row_map[t]+=1
            
        ans = 0
        for j in range(len(grid[0])):
            cols = []
            for row in grid:
                cols.append(row[j])
            t = tuple(cols)
            if t in row_map:
                ans += row_map[t]
                       
        return ans