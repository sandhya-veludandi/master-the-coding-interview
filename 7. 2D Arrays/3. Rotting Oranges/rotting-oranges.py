class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        queue = []
        num_of_min = 0
        size = 0
        num_of_fresh_oranges = 0
        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                if grid[row][col] == 2:
                    queue.append([row, col])
                    size += 1
                elif grid[row][col] == 1: 
                    num_of_fresh_oranges += 1
        
        while queue != []:
            row = queue[0][0]
            col = queue[0][1]
            queue = queue[1:]
            size -= 1
            for direction in directions: 
                row1 = row + direction[0]
                col1 = col + direction[1]
                if row1 < 0 or row1 >= len(grid) or col1 < 0 or col1 >= len(grid[0]) or grid[row1][col1] != 1: 
                    continue
                else: 
                    grid[row1][col1] = 2
                    num_of_fresh_oranges -= 1
                    queue.append([row1, col1])
            if size == 0: 
                num_of_min += 1
                size = len(queue)
            
                
        if num_of_fresh_oranges > 0: 
            return -1
        
        if num_of_min == 0: 
            return 0
        return num_of_min - 1