class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def check(t):
            h = 0

            for wt in workerTimes:
                h += int(sqrt(2 * t / wt + 1 / 4) - 1 / 2)
            
            return h >= mountainHeight
        
        l = 0
        r = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        idx = -1

        while l <= r:
            m = (l + r) // 2

            if check(m):
                idx = m
                r = m - 1
            else:
                l = m + 1
        
        return idx