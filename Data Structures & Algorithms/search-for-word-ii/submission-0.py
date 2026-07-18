class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        res = []
        def backtrack(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]):
                return False
            board[r][c] = '*'
            recurs = (backtrack(r + 1, c, i + 1)or backtrack(r - 1 , c, i + 1)or  
                    backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1))
            board[r][c] = word[i]
            return recurs
        for word in words:
            flag = False
            for row in range(rows):
                if flag:break
                for col in range(cols):
                    if board[row][col] != word[0]:
                        continue
                    if backtrack(row, col,0):
                        res.append(word)
                        flag = True
                        break
        return res
