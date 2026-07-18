class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        
        visited = set()
        def dfs(r,c):
            if (r not in range(rows) or 
            c not in range(cols) or 
            (r,c) in visited or
            grid[r][c] == 0
            ):
                return 0
            visited.add((r,c))
            return (1 + dfs(r + 1, c)+ dfs(r - 1, c) + dfs(r , c + 1) + dfs(r,c- 1))


        area = 0
        for r in range(rows):
            for c in range(cols):

                area = max(area , dfs(r,c))
        return area