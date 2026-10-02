class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        cur = []

        def backtrack(open, closed):
            if open == closed == n:
                res.append("".join(cur))
                return 
            
            if open > n or closed > n:
                return

            if open < n:
                cur.append('(')
                backtrack(open + 1, closed)
                cur.pop()
            
            if closed < open:
                cur.append(')')
                backtrack(open, closed + 1)
                cur.pop()
        
        backtrack(0, 0)
        return res