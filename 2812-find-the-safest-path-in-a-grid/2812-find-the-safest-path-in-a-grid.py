class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        
        if parent_a == parent_b:
            return False
        
        if self.size[parent_a] < self.size[parent_b]:
            self.parent[parent_a] = parent_b
            self.size[parent_b] += self.size[parent_a]
        else:
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]
        
        return True

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return 0
        
        queue = deque()
        distances = [[float("inf") for j in range(n)] for i in range(n)]

        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    queue.append((r, c))
                    distances[r][c] = 0
        
        directions = [(1, 0 ), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if 0 <= row < n and 0 <= col < n and distances[row][col] == float("inf"):
                    distances[row][col] = 1 + distances[r][c]
                    queue.append((row, col))
        
        distance_cells = []

        for r in range(n):
            for c in range(n):
                distance_cells.append((distances[r][c], r, c))
        
        distance_cells.sort(reverse = True)

        union_find = UnionFind(n * n)

        for distance, r, c in distance_cells:
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if 0 <= row < n and 0 <= col < n and distances[row][col] >= distance:
                    union_find.union(r * n + c, row * n + col)
            
            if union_find.find(0) == union_find.find(n * n - 1):
                return int(distance)
        
        return 0