class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0
        lastEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start >= lastEnd:
                lastEnd = end
            else:
                lastEnd = min(lastEnd, end)
                res += 1
        
        return res