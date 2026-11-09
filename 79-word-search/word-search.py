class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, k) -> bool:
            """
            (i, j) - current position
            k - current index of the word
            """
            if k == len(word):
                return True
            elif i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False
            
            val = board[i][j]
            board[i][j] = ""

            if dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1):
                return True # if word has been found
            
            # If no word found
            board[i][j] = val
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False

