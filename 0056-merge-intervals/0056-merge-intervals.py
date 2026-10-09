class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            lastEnd = res[-1][1]

            if start <= lastEnd:
                lastEnd = max(end, lastEnd)
                res[-1][1] = lastEnd
            else:
                res.append([start, end])
        
        return res