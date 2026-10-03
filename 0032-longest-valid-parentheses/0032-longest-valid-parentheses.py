class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        n = len(s)

        lCount = 0
        rCount = 0

        for i in range(n):
            if s[i] == '(':
                lCount += 1
            else:
                rCount += 1
            
            if lCount == rCount:
                res = max(res, lCount + rCount)
            elif rCount > lCount:
                lCount = 0
                rCount = 0
        
        lCount = 0
        rCount = 0

        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                lCount += 1
            else:
                rCount += 1
            
            if lCount == rCount:
                res = max(res, lCount + rCount)
            elif lCount > rCount:
                lCount = 0
                rCount = 0
        
        return res