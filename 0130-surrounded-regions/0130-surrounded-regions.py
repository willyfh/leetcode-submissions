class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def mark(i, j):
            if i <0 or j <0 or i==len(board) or j==len(board[0]):
                return
            if board[i][j] == "#" or board[i][j] == "X":
                return 
            board[i][j] = "#"
            mark(i+1, j)
            mark(i, j+1)
            mark(i-1, j)
            mark(i, j-1)
        
        for j  in range(len(board[0])):
            if board[0][j] == "O":
                mark(0, j)
            if board[len(board)-1][j] == "O":
                mark(len(board)-1, j)
        
        for i  in range(len(board)):
            if board[i][0] == "O":
                mark(i, 0)
            if board[i][len(board[0])-1] == "O":
                mark(i, len(board[0])-1)
                    
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"