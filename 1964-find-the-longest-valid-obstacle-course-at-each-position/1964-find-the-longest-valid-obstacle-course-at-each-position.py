class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        dp = [10 ** 8] * (len(obstacles) + 1)

        for n in obstacles:
            idx = bisect.bisect(dp, n)
            res.append(idx + 1)
            dp[idx] = n

        return res        