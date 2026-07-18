class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        # rows_seen = defaultdict(set)
        # cols_seen = defaultdict(set)
        # diag_seen = defaultdict(set)
        res = []
        #first we check for then rows for any duplicates
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != '.':
                    res += [(i, ele), (ele,j), ( i//3, j//3, ele)]
                '''
                if (board[row][col] == '.':
                    continue
                if board[row][col] in rows_seen:
                        return False
                rows_seen[row].add(board[row][col])
            
        
      
                cols_seen[col].add(board[row][col])
       
                diag_seen[(row//3, col//3)].add(board[row][col])
                '''
        return len(set(res)) == len(res)
        #first we check for then cols for any duplicates
        #first we check for diagonls fo any duplicates 