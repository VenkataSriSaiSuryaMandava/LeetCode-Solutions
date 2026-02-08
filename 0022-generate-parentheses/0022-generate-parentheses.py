class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(subset))
                return
            if openN < n:
                subset.append('(')
                backtrack(openN + 1, closeN)
                subset.pop()
            if closeN < openN:
                subset.append(')')
                backtrack(openN, closeN + 1)
                subset.pop()
        backtrack(0, 0)
        return res