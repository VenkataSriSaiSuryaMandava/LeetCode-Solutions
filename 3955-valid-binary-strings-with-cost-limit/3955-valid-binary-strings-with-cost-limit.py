class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res = []

        def backtrack(i, prev, cost, path):
            if cost > k:
                return

            if i == n:
                res.append("".join(path))
                return

            path.append("0")
            backtrack(i + 1, False, cost, path)
            path.pop()

            if not prev:
                path.append("1")
                backtrack(i + 1, True, cost + i, path)
                path.pop()

        backtrack(0, False, 0, [])
        return res