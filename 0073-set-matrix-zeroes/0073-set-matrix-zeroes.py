class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zeroes = set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroes.add((r, c))

        for r, c in zeroes:
            for i in range(cols):
                matrix[r][i] = 0
            for j in range(rows):
                matrix[j][c] = 0