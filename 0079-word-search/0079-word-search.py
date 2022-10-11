class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(i,j, k, s, board, direct, visit):
            if i<0 or j<0 or i>=len(board) or j >=len(board[0]):
                return False
            if visit[i][j]:
                return False
            visit[i][j] = 1
            
            temp = s + board[i][j]
            if temp == word[:k]:
                s = temp
                if len(temp) == len(word):
                    return True
            else:
                return False
           
            if helper(i+1, j, k+1, s, board, 1, [row[:] for row in visit]) and direct != 3:
                return True
            if helper(i, j+1, k+1, s, board, 2, [row[:] for row in visit]) and direct != 4:
                return True
            if helper(i-1, j, k+1, s, board, 3, [row[:] for row in visit]) and direct != 1:
                return True
            if helper(i,j-1, k+1, s, board, 4, [row[:] for row in visit]) and direct != 2:
                return True
            return False
        
        
        # checking wether all characters in the word can be represented by the board or not
        # if not, return False
        dicti = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in dicti:
                    dicti[board[i][j]] = 0
                dicti[board[i][j]] += 1
              
        for w in word:
            if w not in dicti:
                return False
            if dicti[w]>0:
                dicti[w]-=1
            else:
                return False
            
        # the recursive process to search the word in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i,j,1, "", board,0, [[0] * len(board[0]) for z in range(len(board))]):
                    return True
                
        return False