class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        fr = [[] for i in range(n)]
        to = [[] for i in range(n)]
        
        for conn in connections:
            fr[conn[0]].append(conn[1])
            to[conn[1]].append(conn[0])
            
        
        self.ans = 0
        
        self.visited = {}
        
        self.helper(0, fr, to)
        
        return self.ans
        
        
    def helper(self, i, fr, to):
        
        if i in self.visited:
            return
        
        self.visited[i] = 1
        
        for j in fr[i]:
            if j not in self.visited:
                self.ans += 1
                self.helper(j, fr, to)
        for j in to[i]:
            if j not in self.visited:
                self.helper(j, fr, to)
                