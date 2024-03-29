class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        q = deque()
        
        visited = [False]*(amount+1)
        visited[True] # for zero value
        
        for c in coins:
            if c <= amount:
                q.append((c,1))
        
        while len(q)>0:
            curr, lvl = q.popleft()
            
            if visited[curr]:
                continue
            visited[curr] = True
                    
            if curr==amount:
                return lvl
                
            for c in coins:
                
                t = c + curr
                if t <= amount:
                    q.append((t, lvl+1))
        return -1