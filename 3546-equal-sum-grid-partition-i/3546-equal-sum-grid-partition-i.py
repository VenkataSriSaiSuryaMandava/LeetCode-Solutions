class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        totalSum = 0
        for r in range(rows):
            for c in range(cols):
                totalSum += grid[r][c]
        
        if totalSum % 2:
            return False
        
        prefixSum = 0
        for r in range(rows):
            for c in range(cols):
                prefixSum += grid[r][c]
            
            if prefixSum == totalSum // 2 and r != rows - 1:
                return True
        
        prefixSum = 0
        for c in range(cols):
            for r in range(rows):
                prefixSum += grid[r][c]
            
            if prefixSum == totalSum // 2 and c != cols - 1:
                return True
        
        return False