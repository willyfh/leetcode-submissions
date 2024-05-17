class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        visited = [[False] * len(grid1[0]) for _ in range(len(grid1))]
        
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid2) or j >= len(grid2[0]) or visited[i][j] or grid2[i][j] == 0:
                return True
            
            if grid1[i][j] == 0:
                return False
            
            visited[i][j] = True
            
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            
            return up and down and left and right
            
            
            
            
        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                
                if grid2[i][j] == 1 and not visited[i][j]:
                    if dfs(i, j):
                        ans+=1
        return ans