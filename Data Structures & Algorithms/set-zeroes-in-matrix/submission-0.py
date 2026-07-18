class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])
        row_flag = [False] * rows
        col_flag = [False] * cols
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    col_flag[col] = True
                    row_flag[row] = True
        for row in range(rows):
            for col in range(cols):
                if row_flag[row] or col_flag[col]:
                    matrix[row][col] = 0
        

