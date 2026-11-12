class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def isValidRowOrColumn(board, index, is_row=True):
            seen = set()
            if is_row: # check if valid row
                for j in range(len(board[0])):
                    number = board[index][j] 
                    if number in seen and number != '.':
                        return False
                    seen.add(number)
            else: # check if valid col
                for i in range(len(board)): # check if valid col
                    number = board[i][index]  
                    if number in seen and number != '.':
                        return False
                    seen.add(number)

            return True

        num_rows = len(board)
        num_cols = len(board[0])

        for r in range(9):
            if not isValidRowOrColumn(board, r, is_row=True):
                return False

        for c in range(9):
            if not isValidRowOrColumn(board, c, is_row=False):
                return False

        for start_r in (0, 3, 6):
            for start_c in (0, 3, 6):
                seen = set()
                for r in range(start_r, start_r + 3):
                    for c in range(start_c, start_c + 3):
                        cell = board[r][c]
                        if cell != '.':
                            if cell in seen:
                                return False
                            seen.add(cell)

        return True
