class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        res = []

        def backtrack(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            
            for ch in digitToChar[digits[i]]:
                backtrack(i + 1, cur + ch)
        
        backtrack(0, "")

        return res