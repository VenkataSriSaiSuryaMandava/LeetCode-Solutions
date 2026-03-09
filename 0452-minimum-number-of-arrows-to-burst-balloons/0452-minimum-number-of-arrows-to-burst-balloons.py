class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = len(points)
        prev = points[0]

        for i in range(1, len(points)):
            cur = points[i]

            if cur[0] <= prev[1]:
                res -= 1
                prev = [cur[0], min(prev[1], cur[1])]
            else:
                prev = cur
        
        return res