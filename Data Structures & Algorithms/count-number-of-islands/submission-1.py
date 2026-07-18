class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0
        def dfs(row,col):
            if (row not in range(rows) or col not in range(cols) or grid[row][col] == '0' or (row,col) in visited):
                return
            visited.add((row,col))
            
            dir = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in dir:
                dfs(dr+row,dc +col)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visited:
                    dfs(row,col)
                    island += 1
        return island

