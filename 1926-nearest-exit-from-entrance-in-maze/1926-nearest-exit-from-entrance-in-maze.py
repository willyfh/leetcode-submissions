class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        q = deque()
        
        q.append((entrance[0], entrance[1]))
        
        visited = set()
        
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        step = 0 
        
        
        m = len(maze)
        n = len(maze[0])
        while len(q) > 0:
            
            num_level = len(q)
            for k in range(num_level):
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                # check exit
                if (j==0 or j==n-1 or i==0 or i==m-1) and not (i==entrance[0] and j==entrance[1]):
                    return step

                for x, y in moves:
                    next_i = i+x
                    next_j = j+y
                    if (next_i, next_j) in visited:
                        continue
                    # move to empty cell
                    if next_i>=0 and next_i<m and next_j>=0 and next_j<n and maze[next_i][next_j] == '.':
                        q.append((next_i, next_j))
                        
            step += 1
            
        return -1
        