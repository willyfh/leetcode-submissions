class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def countNeigh(x, y):
            c = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i>=0 and i<len(board) and j>=0 and j <len(board[0]):
                        if  not (i==x and j==y):
                            c+=board[i][j]       
            temp[x][y] = c            
    
        
        temp = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                countNeigh(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                c = temp[i][j]
                if c<2:
                    board[i][j] = 0
                elif c==3:
                    board[i][j] = 1
                elif c>3:
                    board[i][j] = 0
                else:
                    board[i][j] = board[i][j]
                
                