class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        m = len(grid)
        n = len(grid[0])
        
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        num_fresh = 0
        visited = set()
        # find the fresh oranges located next to rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_fresh += 1
                    rotten_adj = False
                    for neigh in neighbors:
                        next_i = i + neigh[0]
                        next_j = j + neigh[1]
                        if next_i >=0 and next_i <m and next_j>=0 and next_j <n:
                            if grid[next_i][next_j] == 2:
                                rotten_adj = True
                                break
                    if rotten_adj:
                        q.append((i, j))
                        visited.add((i,j))
                        
        minute = 0
        while len(q) > 0:
            num_level = len(q)
            minute += 1
            for k in range(num_level):
                i, j = q.popleft()

                num_fresh -= 1
                
                for neigh in neighbors:
                    next_i = i + neigh[0]
                    next_j = j + neigh[1]
                    if next_i >=0 and next_i <m and next_j>=0 and next_j <n:
                        if grid[next_i][next_j] == 1 and (next_i, next_j) not in visited:
                            q.append((next_i, next_j))
                            visited.add((next_i, next_j))
                            
        if num_fresh>0:
            return -1
        
        return minute
                                
                                
                                
                                
                                
                                
                                
                                
                                