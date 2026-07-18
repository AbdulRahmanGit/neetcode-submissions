class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        #way = set()
        def dfs(r,c, i):
            if i == len(word):
                return True
            if (min(r,c) < 0 or rows <= r 
                or cols <= c 
                or word[i] != board[r][c] 
                or board[r][c] == '#'):
                return False
            #way.add((r,c))
            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or 
            dfs(r - 1, c, i + 1) or 
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))
            #way.remove((r,c))
            board[r][c] = word[i]
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(row,col, 0):
                    return True
        return False