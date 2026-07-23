class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        idea: treat each row, column, and 3x3 grid as the check duplicates problem

        1. check the rows
        2. check the columns
        3. check the 3x3 arrays

        '''
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in squares[(i // 3, j // 3)]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
        
        return True
