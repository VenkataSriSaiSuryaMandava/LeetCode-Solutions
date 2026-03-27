class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows = len(mat)
        cols = len(mat[0])

        for r in range(rows):
            for c in range(cols):
                if r % 2:
                    if mat[r][c] != mat[r][(c + k) % cols]:
                        return False
                else:
                    if mat[r][c] != mat[r][(c - k + cols) % cols]:
                        return False
        
        return True
