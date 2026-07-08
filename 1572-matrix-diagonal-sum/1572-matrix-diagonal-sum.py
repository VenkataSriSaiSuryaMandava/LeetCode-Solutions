class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)

        for r in range(n):
            for c in range(n):
                if r == c or r + c == n - 1:
                    res += mat[r][c]
        
        return res