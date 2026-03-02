class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = [-1] * len(grid)

        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    pos[i] = j
                    break
        
        res = 0

        for i in range(n):
            k = - 1

            for j in range(i, n):
                if pos[j] <= i:
                    res += (j - i)
                    k = j
                    break
            
            if k == -1:
                return -1
            else:
                for j in range(k, i, -1):
                    pos[j], pos[j - 1] = pos[j - 1], pos[j]

        return res