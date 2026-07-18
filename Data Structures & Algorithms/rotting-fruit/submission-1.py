class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = time = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row,col))
        directions = [[0,1],[0,-1], [1,0],[-1,0]]
        while fresh > 0 and q:

            length = len(q)
            for i in range(length):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and 
                        nc in range(cols) and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
