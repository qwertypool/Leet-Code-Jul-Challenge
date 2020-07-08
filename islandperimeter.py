
def islandPerimeter( grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        corner = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area += 1
                    if i > 0 and grid[i-1][j] == 1:
                        corner += 1
                    if j > 0 and grid[i][j-1] == 1:
                        corner += 1
        perimeter = area * 4 - corner * 2
        return perimeter

