class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_of_islands = 0
        queue = []
        # Perform sequential search to find 1's, and pass row + col into bfs
        for row in range(len(grid)): 
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    queue.append([row, col])
                    self.bfs(grid, queue)
                    num_of_islands += 1
                    queue = []
        return num_of_islands
    
    def bfs(self, grid, queue): 
        #               up      right   down     left
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        while queue != []:
            row = queue[0][0]
            col = queue[0][1]
            grid[row][col] = "2"
            queue = queue[1:]
            for direction in directions: 
                row1 = row + direction[0]
                col1 = col + direction[1]
                # check if the direction is out of bounds or visited
                if row1 < 0 or row1 >= len(grid) or col1 < 0 or col1 >= len(grid[0]) or grid[row1][col1] == "0" or grid[row1][col1] == "2": 
                    continue
                else: 
                    grid[row1][col1] = "2"
                    queue.append([row1, col1])  