class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += 4
                    if row + 1 < rows and grid[row+1][col] == 1:
                        perimeter -= 2
                    if col + 1 < cols and grid[row][col+1] == 1:
                        perimeter -= 2   
        return perimeter
        