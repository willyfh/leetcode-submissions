class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {}
        col_dict = {}
        box_dict = {}
        
        for i in range(9):
            row_dict[i] = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                # check row
                if board[i][j] in row_dict[i]:
                    return False
                else:
                    row_dict[i].add( board[i][j])
                    
                # check column
                if j not in col_dict:
                    col_dict[j] = set()
                
                if board[i][j] in col_dict[j]:
                    return False
                else:
                    col_dict[j].add(board[i][j])
                    
                # check box
                box_id = str(i//3)+"-"+str(j//3)
                if box_id not in box_dict:
                    box_dict[box_id] = set()
                    
                if board[i][j] in box_dict[box_id]:
                    return False
                else:
                    box_dict[box_id].add(board[i][j])
        return True
                
                    
                