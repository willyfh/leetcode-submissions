class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = {}
        q = deque()
        
        
        q.append(0)
        
        while len(q) > 0:
            
            curr = q.popleft()
            
            visited[curr] = 1
            
            for i in rooms[curr]:
                
                if i in visited:
                    continue
                visited[i] = 1
                q.append(i)
                
        return len(visited) == len(rooms)
                
                
                
                
            
            