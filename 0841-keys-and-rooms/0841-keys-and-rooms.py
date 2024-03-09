class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        self.visited = {}
        
        self.helper(rooms, 0)
        
        return len(self.visited) == len(rooms)
        
        
    def helper(self, rooms, i):              
        
        if i in self.visited:
            return
        self.visited[i] = 1
        for j in rooms[i]:
            if j in self.visited:
                continue            
            self.helper(rooms, j)
            