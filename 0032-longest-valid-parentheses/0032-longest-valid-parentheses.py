class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lCount = 0
        rCount = 0
        res = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                lCount += 1
            else:
                rCount += 1
            
            if lCount == rCount:
                res = max(res, lCount + rCount) 
            elif rCount > lCount:
                lCount = 0
                rCount = 0
            
            i += 1
        
        lCount = 0
        rCount = 0

        i = len(s) - 1
        while i >= 0:
            if s[i] == '(':
                lCount += 1
            else:
                rCount += 1
            
            if lCount == rCount:
                res = max(res, lCount + rCount)
            elif lCount > rCount:
                lCount = 0
                rCount = 0
            
            i -= 1
        
        return res