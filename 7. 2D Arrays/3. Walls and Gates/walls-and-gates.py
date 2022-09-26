class Solution(object):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    def wallsAndGates(self, a, n, m): 
        for row in range(n):
            for col in range(m):
                if a[row][col] == 0:
                    self.dfs(row, col, a, 0)
        return a
        
    def dfs(self, row, col, grid, steps): 
        steps += 1
        for direction in self.directions:
            row1 = row + direction[0]
            col1 = col + direction[1]
            if row1 < 0 or row1 >= len(grid) or col1 < 0 or col1 >= len(grid[0]) or grid[row1][col1] <= 0 or steps > grid[row1][col1]:
                continue
            else:
                grid[row1][col1] = min(steps, grid[row1][col1])
                self.dfs(row1, col1, grid, steps)