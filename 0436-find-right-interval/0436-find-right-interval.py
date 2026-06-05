class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, interval in enumerate(intervals):
            interval.append(i)
        
        intervals.sort()
        res = [-1] * len(intervals)

        for start, end, index in intervals:
            l = 0
            r = len(intervals) - 1
            idx = -1

            while l <= r:
                m = (l + r) // 2

                if intervals[m][0] >= end:
                    idx = m
                    r = m - 1
                else:
                    l = m + 1
            
            if idx != -1:
                res[index] = intervals[idx][2]
        
        return res