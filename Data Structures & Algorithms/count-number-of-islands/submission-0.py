class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r,c):
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or grid[r][c] == '0':
                return 0
            grid[r][c] = '0'
            dfs(r - 1,c)
            dfs(r + 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
            return 1
        count = 0
        for r in range(rows):
            for c in range(cols):
                count += dfs(r,c)
        return count