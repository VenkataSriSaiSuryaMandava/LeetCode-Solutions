class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        subset = []

        def backtrack(left, right):
            if left == right == n:
                res.append("".join(subset))
                return
            
            if left < n:
                subset.append('(')
                backtrack(left + 1, right)
                subset.pop()
            if right < left:
                subset.append(')')
                backtrack(left, right + 1)
                subset.pop()
        
        backtrack(0, 0)

        return res