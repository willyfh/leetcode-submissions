class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        self.visited = {}
        self.ans = 0
        n = len(isConnected)
        
        for i in range(n):
            if i in self.visited:
                continue
            self.ans +=1
            self.visit_province(i, isConnected)
                
        return self.ans
                
    def visit_province(self, i, isConnected):
        
        self.visited[i] = 1
        
        for j,v in enumerate(isConnected[i]):
            if j in self.visited or v == 0:
                continue
                        
            self.visit_province(j, isConnected)