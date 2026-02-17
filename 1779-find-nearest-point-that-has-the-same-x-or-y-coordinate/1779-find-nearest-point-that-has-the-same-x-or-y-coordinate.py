class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        best_index = -1
        best_dist = float('inf')

        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                dist = abs(a - x) + abs(b - y)
                if dist < best_dist:
                    best_dist = dist
                    best_index = i
        return best_index