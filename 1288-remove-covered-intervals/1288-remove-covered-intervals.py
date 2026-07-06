class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prev_start, prev_end = res[-1]

            if prev_start > start or end > prev_end:
                res.append([start, end])
        
        return len(res)