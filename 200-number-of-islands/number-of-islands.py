class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Use DFS to solve problem - want to explore all cells in the grid & mark all connected land cells 
        if not grid: 
            return 0

        count = 0 # number of islands

        # Define a DFS function that takes the grid & current cell coords (i, j)
        def explore(grid, i, j):
            grid_width = len(grid) # number of rows
            grid_len = len(grid[0]) # number of cols

            # if cell is out of bounds or not land (1)
            if i < 0 or i >= grid_width or j < 0 or j >= grid_len or grid[i][j] == '0':
                return
            
            # Mark current cell as visited
            grid[i][j] = '0'

            # Recrusively call DFS for neighboring cells to explore
            explore(grid, i-1, j) # up
            explore(grid, i+1, j) # down
            explore(grid, i, j-1) # left
            explore(grid, i, j+1) # right

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    explore(grid, i, j)
        
        return count

        