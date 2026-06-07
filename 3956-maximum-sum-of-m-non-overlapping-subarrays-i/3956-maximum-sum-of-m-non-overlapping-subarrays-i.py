class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        NEG = -10 ** 30

        dp = [0] * (n + 1)
        res = NEG

        for _ in range(1, m + 1):
            newDP = [NEG] * (n + 1)
            queue = deque()

            for i in range(1, n + 1):
                newDP[i] = newDP[i - 1]

                j = i - l
                if j >= 0 and dp[j] != NEG:
                    val = dp[j] - pref[j]

                    while queue and queue[-1][1] <= val:
                        queue.pop()
                    queue.append((j, val))

                while queue and queue[0][0] < i - r:
                    queue.popleft()

                if queue:
                    newDP[i] = max(newDP[i], pref[i] + queue[0][1])

            res = max(res, newDP[n])
            dp = newDP

        return res