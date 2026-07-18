class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            #append the first row
            res += matrix.pop(0)
            #append the last columns vertically
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            #append the last row in reverse order
            if matrix:
                res += matrix.pop()[::-1]
            #append the first col in reverse vertically
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
            # goto first step
        return res