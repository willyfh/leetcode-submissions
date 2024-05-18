class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        visited = [[False] * len(land[0]) for _ in range(len(land))]
        
        def dfs(i, j, max_i, max_j):
            
            if i < 0 or j < 0 or i>=len(land) or j >= len(land[0]) or land[i][j] == 0 or visited[i][j]:
                return [max_i, max_j]
            
            visited[i][j] = True
            
            max_i = max(max_i, i)
            max_j = max(max_j, j)
            
            right = dfs(i, j+1, max_i, max_j)
            down = dfs(i+1, j, right[0], right[1])
            
            return down
            
        
        ans = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1 and not visited[i][j]:
                    farmland = dfs(i, j, i, j)
                    ans.append([i, j, farmland[0], farmland[1]])
                    
        return ans