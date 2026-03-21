class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for c in range(y, y + k):
            l = x
            r = x + k - 1

            while l < r:
                grid[l][c], grid[r][c] = grid[r][c], grid[l][c]
                l += 1
                r -= 1
        
        return grid
