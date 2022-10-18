class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        i=0
        j=0
        flip = [[True for x in range(len(board[0]))] for y in range(len(board))]
        visited =  [[False for x in range(len(board[0]))] for y in range(len(board))]
        
        
        def helper(x, y):
            if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
                return
            if visited[x][y]:
                return
            
            visited[x][y] = True
            
            if board[x][y] == "O":
                
                flip[x][y] = False
                helper(x-1, y)
                helper(x+1, y)
                helper(x, y-1)
                helper(x, y+1)
        
        for j in range(len(board[0])):
            if board[0][j] == "O":
                helper(0,j)
                
        for j in range(len(board[0])):
            if board[-1][j] == "O":
                helper(len(board)-1,j)
                
        for i in range(len(board)):
            if board[i][0] == "O":
                helper(i,0)
                
        for i in range(len(board)):
            if board[i][-1] == "O":
                helper(i,len(board[0])-1)
                
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if flip[i][j]:
                    board[i][j] = "X"
                
                
            
            