class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = [points[0]]
        
        for start, end in points:
            if start <= res[-1][1]:
                res[-1][1] = min(res[-1][1], end)
            else:
                res.append([start, end])
        
        return len(res)