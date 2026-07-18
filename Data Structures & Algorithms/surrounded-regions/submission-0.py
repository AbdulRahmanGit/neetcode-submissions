class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        
        q = deque()
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    q.append((r, c))
        for c in range(cols):
            for r in [0, rows - 1]:
                if board[r][c] == 'O':
                    q.append((r, c))
        dir = [[0,1],[0,-1],[-1,0],[1,0]]
        
        while q:
            r,c = q.popleft()
            
            if (0 <= r < rows and 0 <= c < cols  and board[r][c]=='O'):
                board[r][c] = 'S'
                for dr, dc in dir:
                    q.append((dr + r,dc + c))
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] ='X'
                if board[row][col] == 'S':
                    board[row][col] ='O'


