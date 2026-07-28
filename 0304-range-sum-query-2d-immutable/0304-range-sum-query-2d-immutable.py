class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix = [[0 for c in range(cols + 1)] for r in range(rows + 1)]

        for r in range(rows):
            prefix = 0

            for c in range(cols):
                prefix += matrix[r][c]
                above = self.prefix[r][c + 1]
            
                self.prefix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        topleft = self.prefix[row1 - 1][col1 -1]
        bottomright = self.prefix[row2][col2]
        above = self.prefix[row1 - 1][col2]
        left = self.prefix[row2][col1 - 1]

        return topleft + bottomright - above - left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)