class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        self.visited = {}
        self.ans = 0
        n = len(isConnected)
        for i in range(n):
            for j in range(i, n):
                if (i, j) in self.visited or isConnected[i][j] == 0 :
                    continue
                    
                self.ans += 1
                self.visit_province((i,j), isConnected)
                
        return self.ans
                
    def visit_province(self, tup, isConnected):
        i,j = tup
        self.visited[(i,j)] = 1
        # visited[(j,i)] = 1 
        
        for k,v in enumerate(isConnected[j]):
            if (j,k) in self.visited or isConnected[j][k] == 0:
                continue
            
            self.visited[(j,k)] = 1
            self.visit_province((j,k), isConnected)